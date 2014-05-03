#! /usr/bin/env python

import os
import coma
import qca
import numpy
import collections
import scipy.optimize
from IPython.parallel import require

class InfiniteWireFindCriticalPoint(object):
    def __init__(self):
        self.s = None
        self.epsilon = 1E-3
        self.N = None
        self.boa = None
        self.q = 0
        self.T = None
        self.N_dead = 100
        self.V1s_start = (1,100)
        self.model_type = 'QcaIsing'
        
        self.y0s = []
        self.e_y0s = []
        self.ss = []
        self.e_ss = []
        
        self.program = 'InfiniteWireFindCriticalPoint'
        self.version = None
        self.results = collections.OrderedDict()
    
    def f_P(self, V1, P):
        self.s.l = qca.InfiniteWire(self.N, self.N_dead, V1, self.boa, P)
        self.s.init()
        self.s.run()
        Ps = self.s.results['P']
        return sum(Ps)/len(Ps) - P

    def fit_line(self, V1, f):
        xs2 = numpy.array([1E-6,5E-6,10E-6])
        ys2 = numpy.array([f(V1, x) for x in xs2])
        f_line = lambda x,a,b: a+b*x
        a,cov = scipy.optimize.curve_fit(f_line,xs2,ys2,(0.1,0.1))
        if not isinstance(cov, float):
            error_rel = numpy.sqrt(cov.diagonal() / a**2)
            return ((a[0],error_rel[0]),(a[1],error_rel[1]))
        else:
            return ((a[0],numpy.inf),(a[1],numpy.inf))

    def slope(self, V1):
        (y0,e_y0),(s,e_s) = self.fit_line(V1, self.f_P)
        self.y0s.append(y0)
        self.e_y0s.append(e_y0)
        self.ss.append(s)
        self.e_ss.append(e_s)
        #print('Slope for V1 = {}: {}'.format(V1, s))
        return s
    
    def init(self):
        pass
    
    def run(self, V1s_start=None):
        if self.model_type == 'QcaIsing':
            self.s = qca.QcaIsing()
        elif self.model_type == 'QcaBond':
            self.s = qca.QcaBond()
        self.s.V0 = 1E6
        self.s.T = self.T
        self.s.q = self.q
        
        self.y0s = []
        self.e_y0s = []
        self.ss = []
        self.e_ss = []
        
        if V1s_start is not None:
            self.V1s_start = V1s_start
        V11 = self.V1s_start[0]
        V12 = self.V1s_start[1]
        try:
            V1_crit = scipy.optimize.bisect(self.slope, V11, V12, xtol=self.epsilon)
            
            self.results['V1_crit'] = V1_crit
            self.results['N_iteration'] = len(self.y0s)
            self.results['y0'] = self.y0s
            self.results['error_y0'] = self.e_y0s
            self.results['slope'] = self.ss
            self.results['error_slope'] = self.e_ss
        except (ValueError):
            pass
    
    def __getstate__(self):
        i = collections.OrderedDict()
        i['info'] = collections.OrderedDict()
        i['info']['description'] = 'Find the critical V1 for an infinite wire'
        i['parameters'] = collections.OrderedDict()
        i['parameters']['q'] = self.q
        i['parameters']['T'] = self.T
        i['parameters']['N'] = self.N
        i['parameters']['N_dead'] = self.N_dead
        i['parameters']['boa'] = self.boa
        i['parameters']['epsilon'] = self.epsilon
        i['parameters']['V1s_start'] = self.V1s_start
        i['parameters']['model_type'] = self.model_type
        i['parameters']['model'] = self.s
        i['results'] = self.results
        return i
    
    def __setstate__(self, i):
        self.__init__()
        self.s = i['parameters']['model']
        self.q = i['parameters']['q']
        self.T = i['parameters']['T']
        self.N = i['parameters']['N']
        self.N_dead = i['parameters']['N_dead']
        self.boa = i['parameters']['boa']
        self.V1s_start = i['parameters']['V1s_start']
        self.model_type = i['parameters']['model_type']
        self.epsilon = i['parameters']['epsilon']
        self.results = i['results']

    def coma_getstate(self):
        return self.__getstate__()

def define_parameters(e):
    e.define_parameter_set(
            ('m', 'parameters/model_type'),
            ('T', 'parameters/T'),
            ('N', 'parameters/N'),
            ('boa','parameters/boa'))
    T = 2.0
    Ns = range(1,13)
    boas = [1.2,2.0]
    m = 'QcaIsing'
    for N in Ns:
        for boa in boas:
            e.add_parameter_set(m,T,N,boa)
    
    Ns = range(1,6)
    m = 'QcaBond'
    for N in Ns:
        for boa in boas:
            e.add_parameter_set(m,T,N,boa)

@require('qca','numpy','scipy.optimize','collections',InfiniteWireFindCriticalPoint)
def run_it(p):
    print('Running for parameters: {}'.format(p))
    s = InfiniteWireFindCriticalPoint()
    s.model_type = p.m
    s.q = 0.5
    s.T = p.T
    s.N = p.N
    s.boa = p.boa
    s.V1s_start = (0.1,1000)
    s.init()
    s.run()
    return s

def run_experiment(reset=False):
    dir = os.path.dirname(os.path.abspath(__file__))
    c = coma.load_config()
    c['archive_pretty_print'] = False
    
    # e = coma.ParallelExperiment(dir, config=c, profile='onnes_and_macheath')
    e = coma.Experiment(dir, config=c)
    if reset:
        e.reset()
    if not e.isactive():
        e.activate()

    define_parameters(e)
    r,t = e.run(run_it)

    e.deactivate()
    print('Ran {} out of {} measurements'.format(r,t))

if __name__ == '__main__':
    run_experiment(False)
