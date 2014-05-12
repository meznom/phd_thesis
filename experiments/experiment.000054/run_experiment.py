#! /usr/bin/env python

import os
import coma
import qca
import numpy as np
from IPython.parallel import require

def define_parameters(e):
    e.define_parameter_set(
            ('doa','parameters/layout/doa'),
            ('I1','parameters/layout/I1'),
            ('I2','parameters/layout/I2'),
            ('I3','parameters/layout/I3'))
    n = 30
    I_fixed = [-1,1]
    doas = [2.2,2.6]
    Is = np.linspace(-1,1,n)
    for doa in doas:
        for I2 in I_fixed:
            for I1 in Is:
                for I3 in Is:
                    e.add_parameter_set(doa,round(I1,4),round(I2,4),round(I3,4))

@require('qca')
def run_it(p):
    print('Running for parameters: {}'.format(p))
    s = qca.QcaIsing()
    s.q = 0.5
    s.T = 2.0
    N_lead = 2
    V1 = 200
    s.l = qca.MajorityGate(N_lead,V1,p.doa,p.I1,p.I2,p.I3)
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
