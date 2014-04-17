#! /usr/bin/env python

import os
import coma
import qca
import numpy as np
from collections import OrderedDict

def define_parameters(e):
    e.define_parameter_set(
            ('model', 'parameters/model'),
            ('V0', 'parameters/V0'),
            ('mu', 'parameters/mu'),
            ('N', 'parameters/layout/N'),
            ('V1', 'parameters/layout/V1'),
            ('boa', 'parameters/layout/boa'))
    
    e.add_parameter_set('QcaBond',1E6,0,1,30,2)
    e.add_parameter_set('QcaFixedCharge',1E6,0,1,30,2)

    e.add_parameter_set('QcaBond',1E6,0,2,20,2)
    e.add_parameter_set('QcaFixedCharge',1E6,0,2,20,2)
    e.add_parameter_set('QcaBond',1E6,0,2,100,2)
    e.add_parameter_set('QcaFixedCharge',1E6,0,2,100,2)
    
    e.add_parameter_set('QcaFixedCharge',1000,250,2,100,2)
    e.add_parameter_set('QcaGrandCanonical',1000,250,2,100,2)

def run_it(p):
    print('Running for parameters: {}'.format(p))

    s = None
    if p.model == 'QcaBond':
        s = qca.QcaBond()
    elif p.model == 'QcaFixedCharge':
        s = qca.QcaFixedCharge()
    elif p.model == 'QcaGrandCanonical':
        s = qca.QcaGrandCanonical()
    s.V0 = p.V0
    s.mu = p.mu
    s.T = 1
    s.l = qca.Wire(p.N,p.V1,p.boa,1)
    s.init()
    s.run()
    Es = np.array(s.energies())
    Es.sort()
    Es = Es[:10000] # throw away high energy states
    s.results['energies'] = Es

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
