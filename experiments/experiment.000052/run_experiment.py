#! /usr/bin/env python

import os
import coma
import qca
import numpy as np
from IPython.parallel import require

import scipy.optimize
import collections

class FindBoaForPout(object):
    def __init__(self):
        self.T = None
        self.N = None
        self.V1 = None
        self.P_out = None
        self.s = None
        self.results = collections.OrderedDict()
    
    def init(self):
        pass
    
    def P_out_for_boa(self, boa):
        self.s = qca.QcaIsing()
        self.s.t = 1
        self.s.q = 0.5
        P_D = 1.0
        self.s.T = self.T
        self.s.l = qca.Wire(self.N,self.V1,boa,P_D)
        self.s.init()
        self.s.run()
        return self.s.results['P'][-1]
        
    def run(self):
        boa = scipy.optimize.bisect(lambda boa: self.P_out_for_boa(boa)-self.P_out, 1.0, 10.0)
        self.results['boa'] = boa
    
    def coma_getstate(self):
        i = collections.OrderedDict()
        i['info'] = collections.OrderedDict()
        i['info']['description'] = 'Find the right b/a for a given target output polarization.'
        i['parameters'] = collections.OrderedDict()
        i['parameters']['P_out'] = self.P_out
        i['parameters']['model'] = self.s
        i['results'] = self.results
        return i

def define_parameters(e):
    e.define_parameter_set(
            ('T', 'parameters/T'),
            ('N', 'parameters/layout/N'),
            ('V1', 'parameters/layout/V1'))
    
    T = 2.0
    Ns = range(1,13)
    V1s = [150,200,250]
    for N in Ns:
        for V1 in V1s:
            e.add_parameter_set(T,N,V1)

@require('qca','collections','scipy.optimize',FindBoaForPout)
def run_it(p):
    print('Running for parameters: {}'.format(p))

    s = FindBoaForPout()
    s.T = p.T
    s.N = p.N
    s.V1 = p.V1
    s.P_out = 0.9
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
