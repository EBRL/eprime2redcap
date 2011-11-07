#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import numpy as np

from . import io
from . import errors

"""
sctsstc: subject-subject total
sctsotc: subject-object total
sctoc: overall correct (both ss and so)

if len(set(Response.RT)) != 24 BAD

use Response.RT to find the Type and find

"""


F_FMT = '%.3f'
FZ_FMT = '%0.3f'
D_FMT = '%d'


def MR(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)
    
    results = {}
    
    corr = filter(lambda x: x['stim.RESP'] == x['Correct'], dl)
    #  Correct
    results['mrtXltc'] = D_FMT % len(corr)
    #  Correct pct
    results['mrtXltcp'] = F_FMT % ((float(len(corr)) / len(dl)) * 100)
    
    #  RT
    all_rt = np.array([float(x['stim.RT']) for x in dl])
    results['mrtXlmrt'] = F_FMT % np.mean(all_rt)
    results['mrtXlsdrt'] = FZ_FMT % np.std(all_rt)
    
    return results
    
def MI(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)
    
    trials = filter(lambda x: x['runList'] == 'Imagery', dl)

    results = {}

    #  This is static
    results['mitXtt'] = 'new'
    
    #  correct
    corr = filter(lambda x: x['Correct'] == x['stim.RESP'], trials)
    results['mitXtc'] = D_FMT % len(corr)
    #  correct pct
    results['mitXtcp'] = F_FMT % ((float(len(corr)) / len(trials)) * 100)
    
    #  RT
    all_rt = np.array([float(x['stim.RT']) for x in trials])
    results['mitXmrt'] = F_FMT % np.mean(all_rt)
    results['mitXsdrt'] = FZ_FMT % np.std(all_rt)
    
    return results


def OLSON(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)
    
    results = {}
    
    trials = filter(lambda x: x['runList'] == 'Olsen', dl)
    
    corrf = lambda x: (x['stim.RESP'] == 'a' and x['correct'] == '1') or (x['stim.RESP'] == 'l' and x['correct'] == '2')
    incorrf = lambda x: (x['stim.RESP'] == 'a' and x['correct'] != '1') or (x['stim.RESP'] == 'l' and x['correct'] != '2')
    #  Correct
    corr = filter(corrf, trials)
    results['otXtc'] = D_FMT % len(corr)
    results['otXtcp'] = F_FMT % ((float(len(corr)) / len(trials)) * 100)
    
    corr_rt = np.array([float(x['stim.RT']) for x in corr])
    #  Correct mean RT
    results['otXcmrt'] = F_FMT % np.mean(corr_rt)
    #  Correct mean RT SD
    results['otXcsdrt'] = FZ_FMT % np.std(corr_rt)
    
    incorr = filter(incorrf, trials)
    incorr_rt = np.array([float(x['stim.RT']) for x in incorr])
    #  Incorrect mean RT
    results['otXimrt'] = F_FMT % np.mean(corr_rt)
    #  Incorrect mean RT SD
    results['otXisdrt'] = FZ_FMT % np.std(corr_rt)
    
    return results


def FIG(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)
    
    results = {}
    
    corr = filter(lambda x: x['stim.RESP'] == x['Correct'], dl)
    #  Correct
    results['mrtXbtc'] = D_FMT % len(corr)
    results['mrtXbtcp'] = F_FMT % ((float(len(corr)) / len(dl)) * 100)
    
    all_rt = np.array([float(x['stim.RT']) for x in dl])
    results['mrtXbmrt'] = F_FMT % np.mean(all_rt)
    results['mrtXbsdrt'] = FZ_FMT % np.std(all_rt)
    
    return results
    
    
def SENT(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)
    
    results = {}
    
    
    return results
