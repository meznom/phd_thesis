#! /usr/bin/env python

import os
import coma
import qca
import numpy as np
from IPython.parallel import require

def define_parameters(e):
    e.define_parameter_set(
            ('model', 'parameters/model'),
            ('T', 'parameters/T'),
            ('N', 'parameters/layout/N'),
            ('V1', 'parameters/layout/V1'),
            ('boa', 'parameters/layout/boa'))
    
    model = 'QcaIsing'
    T = 2.0
    Ns = range(1,13)
    V1s = [100,200]
    boas = [1.2,1.5,2.0,2.5,3.0]
    for N in Ns:
        for V1 in V1s:
            for boa in boas:
                e.add_parameter_set(model,T,N,V1,boa)

@require('qca')
def run_it(p):
    print('Running for parameters: {}'.format(p))
    s = None
    if p.model == 'QcaIsing':
        s = qca.QcaIsing()
    elif p.model == 'QcaBond':
        s = qca.QcaBond()
    s.q = 0.5
    s.t = 1
    s.T = p.T
    P = 1.0
    s.l = qca.Wire(p.N,p.V1,p.boa,P)
    s.init()
    s.run()
    return s

def run_experiment(reset=False):
    dir = os.path.dirname(os.path.abspath(__file__))
    c = coma.load_config()
    c['archive_pretty_print'] = False
    
    e = coma.ParallelExperiment(dir, config=c, profile='onnes_and_macheath')
    # e = coma.Experiment(dir, config=c)
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
