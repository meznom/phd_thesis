#! /usr/bin/env python

import os
import coma
import qca
import numpy
import collections
import scipy.optimize
from IPython.parallel import require

class InfiniteWireFindSelfConsistentPolarization(object):
    def __init__(self):
        self.s = None
        self.epsilon = 1E-6
        self.T = None
        self.N = None
        self.V1 = None
        self.boa = None
        self.type = None
        self.q = 0
        self.N_dead = 100

        self.program = 'InfiniteWireFindSelfConsistentPolarization'
        self.version = None
        self.results = collections.OrderedDict()
  
    def f(self, P):
        self.s.l = qca.InfiniteWire(self.N, self.N_dead, self.V1, self.boa, P)
        self.s.init()
        self.s.run()
        Ps = self.s.results['P']
        return sum(Ps)/len(Ps) - P

    def init(self):
        pass
  
    def run(self):
        if self.type == 'QcaBond':
            self.s = qca.QcaBond()
        elif self.type == 'QcaIsing':
            self.s = qca.QcaIsing()
        self.s.V0 = 1E6
        self.s.T = self.T
        self.s.q = self.q

        try:
            P_D = scipy.optimize.bisect(self.f, 1E-4, 1, xtol=self.epsilon)
            self.results['P_D'] = P_D
        except (ValueError):
            pass

    def __getstate__(self):
        i = collections.OrderedDict()
        i['info'] = collections.OrderedDict()
        i['info']['description'] = 'Self-consistent polarization for a '\
                                   'semi-infinite wire, using root finding'
        i['parameters'] = collections.OrderedDict()
        i['parameters']['type'] = self.type
        i['parameters']['q'] = self.q
        i['parameters']['T'] = self.T
        i['parameters']['N'] = self.N
        i['parameters']['N_dead'] = self.N_dead
        i['parameters']['V1'] = self.V1
        i['parameters']['boa'] = self.boa
        i['parameters']['epsilon'] = self.epsilon
        i['parameters']['model'] = self.s
        i['results'] = self.results
        return i
    
    def __setstate__(self, i):
        self.__init__()
        self.s = i['parameters']['model']
        self.type = i['parameters']['type']
        self.q = i['parameters']['q']
        self.T = i['parameters']['T']
        self.N = i['parameters']['N']
        self.N_dead = i['parameters']['N_dead']
        self.V1 = i['parameters']['V1']
        self.boa = i['parameters']['boa']
        self.epsilon = i['parameters']['epsilon']
        self.results = i['results']

    def coma_getstate(self):
        return self.__getstate__()

def define_parameters(e):
    e.define_parameter_set(
            ('type', 'parameters/type'),
            ('T', 'parameters/T'),
            ('N', 'parameters/N'),
            ('V1', 'parameters/V1'),
            ('boa','parameters/boa'))
    n1 = 50
    n2 = 100
    T = 2.0
    N = 3
    V1s = numpy.sort(numpy.concatenate((
            numpy.logspace(-3,0,n1) * 4 + 25.99,
            numpy.linspace(25,75,n2)
          )))
    boa = 1.2
    ms = ['QcaBond','QcaIsing']
    for m in ms:
        for V1 in V1s:
            e.add_parameter_set(m,T,N,round(V1,4),boa)
    
    V1s = numpy.sort(numpy.concatenate((
            numpy.logspace(-3,0,n1) * 5 + 107.89,
            numpy.linspace(100,250,n2)
          )))
    boa = 2.0
    ms = ['QcaBond','QcaIsing']
    for m in ms:
        for V1 in V1s:
            e.add_parameter_set(m,T,N,round(V1,4),boa)

@require('qca','numpy','scipy.optimize','collections',InfiniteWireFindSelfConsistentPolarization)
def run_it(p):
    print('Running for parameters: {}'.format(p))
    s = InfiniteWireFindSelfConsistentPolarization()
    s.type = p.type
    s.q = 0.5
    s.T = p.T
    s.N = p.N
    s.V1 = p.V1
    s.boa = p.boa
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
    run_experiment(True)
