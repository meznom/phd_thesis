#! /usr/bin/env python

import os
import coma
import qca
import numpy as np
from collections import OrderedDict

last_s = None
last_ps = []

def define_parameters(e):
    e.define_parameter_set(
            ('model', 'parameters/model'),
            ('V0', 'parameters/V0'),
            ('N', 'parameters/layout/N'),
            ('V1', 'parameters/layout/V1'),
            ('boa', 'parameters/boa'),
            ('T', 'parameters/T'))
    for T in np.linspace(1E-3,4,100):
        e.add_parameter_set('QcaBond',1E6,2,20,2,round(T,4))
    for T in np.linspace(1E-3,4,100):
        e.add_parameter_set('QcaFixedCharge',1E6,2,20,2,round(T,4))
    for T in np.linspace(1E-3,4,100):
        e.add_parameter_set('QcaBond',1E6,2,100,2,round(T,4))
    for T in np.linspace(1E-3,4,100):
        e.add_parameter_set('QcaFixedCharge',1E6,2,100,2,round(T,4))
    for T in np.linspace(0,50,100):
        e.add_parameter_set('QcaFixedCharge',1000,2,100,2,T)
    for T in np.linspace(0,50,100):
        e.add_parameter_set('QcaGrandCanonical',1000,2,100,2,T)

def run_it(p):
    print('Running for parameters: {}'.format(p))

    global last_s
    global last_ps

    if last_ps[:-1] == p.ps[:-1]:
        print('Changed T only')
        s = last_s
        s.T = p.T
        s.run(changedTonly=True)
    else:
        s = None
        if p.model == 'QcaBond':
            s = qca.QcaBond()
        elif p.model == 'QcaFixedCharge':
            s = qca.QcaFixedCharge()
        elif p.model == 'QcaGrandCanonical':
            s = qca.QcaGrandCanonical()
        s.V0 = p.V0
        s.mu = 250
        s.l = qca.Wire(p.N,p.V1,p.boa,1)
        s.T = p.T

        s.init()
        s.run()

    last_s = s
    last_ps = p.ps

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
