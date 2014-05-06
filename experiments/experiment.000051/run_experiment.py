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
            ('boa', 'parameters/layout/boa'),
            ('P', 'parameters/layout/P'))
    
    model = 'QcaIsing'
    T = 2.0
    Ns = [2,4,6,8,10,12]
    V1s = [200]
    Ps = [1.0,0.5,0.1]
    boas = np.linspace(0.1,5.0,50)
    for P in Ps:
        for N in Ns:
            for V1 in V1s:
                for boa in boas:
                    e.add_parameter_set(model,T,N,V1,round(boa,4),P)

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
    s.l = qca.Wire(p.N,p.V1,p.boa,p.P)
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
