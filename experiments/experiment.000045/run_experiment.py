#! /usr/bin/env python

import os
import coma
import qca
import numpy as np
from IPython.parallel import require

def define_parameters(e):
    e.define_parameter_set(
            ('model', 'parameters/model'),
            ('q', 'parameters/q'),
            ('T', 'parameters/T'),
            ('boa', 'parameters/layout/boa'),
            ('P', 'parameters/layout/P'))
    n = 40
    qs = [0.0,0.5]
    boas = [1.2] #[1.2,2.0]
    Ps = np.sort(np.concatenate((np.logspace(-3,-1,n),np.linspace(0,1.0,n))))
    m = 'QcaBond'
    T = 1
    for q in qs:
        for boa in boas:
            for P in Ps:
                e.add_parameter_set(m,q,T,boa,round(P,6))
    m = 'QcaFixedCharge'
    T = 1E-9
    for q in qs:
        for boa in boas:
            for P in Ps:
                e.add_parameter_set(m,q,T,boa,round(P,6))

@require('qca')
def run_it(p):
    print('Running for parameters: {}'.format(p))

    s = None
    if p.model == 'QcaBond':
        s = qca.QcaBond()
    elif p.model == 'QcaFixedCharge':
        s = qca.QcaFixedCharge()
    elif p.model == 'QcaGrandCanonical':
        s = qca.QcaGrandCanonical()

    s.q = p.q
    s.V0 = 1E6
    s.mu = 0
    s.t = 1
    s.T = p.T
    N,V1 = 3,40
    s.l = qca.Wire(N,V1,p.boa,p.P)

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
    run_experiment(True)
