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
    results['mitXtt'] = '2'
    
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
    #  Don't need total percentage
    #  results['otXtcp'] = F_FMT % ((float(len(corr)) / len(trials)) * 100)
    
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

def adjust(mean, sd, rt, thresh=2.5):
    upper = mean + sd * thresh
    lower = mean - sd * thresh
    if rt > upper:
        return upper
    elif rt < lower:
        return lower
    else:
        return rt

def SENT(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)
    
    trials = filter(lambda x: x['Running'] == 'Task', dl)
    all_responses = filter(lambda x: x['DecisionScreen'] == '1', trials)
    ss_responses = filter(lambda x: x['Type'] == 'SubjectSubject', all_responses)
    so_responses = filter(lambda x: x['Type'] == 'SubjectObject', all_responses)

    results = {}
    
    #  Do SS responses first
    ss_cor = 0
    corr_f = lambda x: (x['CorrectAnswer'] == '5' and x['Response.RESP'] == 'f') or (x['CorrectAnswer'] == '1' and x['Response.RESP'] == 't')
    curr_f = lambda x: x['Response.RTTime'] == prev['Response.RTTime'] and x['DecisionScreen'] != '1'
    for i, resp_trial in enumerate(ss_responses):
        #  Find the previous trial
        prev = trials[trials.index(resp_trial)-1]
        #  The current trials are trials that match prev's Response.RTTime and resp_trial
        curr_trials = filter(curr_f, trials) + [resp_trial]
        curr_rt = np.array([float(x['Target.RT']) for x in curr_trials])
        mrt = np.mean(curr_rt)
        rtsd = np.std(curr_rt, ddof=1)
        #  Adjust
        adj_rt = np.array([adjust(mrt, rtsd, x) for x in curr_rt])
        adj_mean = np.mean(adj_rt)
        adj_sd = np.std(adj_rt, ddof=1)
        if adj_mean != mrt:
            rt = adj_mean
            sd = adj_sd
        else:
            rt = mrt
            sd = rtsd
        results['sctss%02dmrt' % (i+1)] = F_FMT % rt
        results['sctss%02dsd' % (i+1)] = F_FMT % sd
        if corr_f(resp_trial):
            ss_cor += 1
    results['sctsstc'] = D_FMT % ss_cor
    
    # Now do SO responses
    so_cor = 0
    for i, resp_trial in enumerate(so_responses):
        #  Find the previous trial
        prev = trials[trials.index(resp_trial)-1]
        #  The current trials are trials that match prev's Response.RTTime and resp_trial
        curr_trials = filter(curr_f, trials) + [resp_trial]
        curr_rt = np.array([float(x['Target.RT']) for x in curr_trials])
        mrt = np.mean(curr_rt)
        rtsd = np.std(curr_rt, ddof=1)
        #  Adjust
        adj_rt = np.array([adjust(mrt, rtsd, x) for x in curr_rt])
        adj_mean = np.mean(adj_rt)
        adj_sd = np.std(adj_rt, ddof=1)
        if adj_mean != mrt:
            rt = adj_mean
            sd = adj_sd
        else:
            rt = mrt
            sd = rtsd
        results['sctso%dmean' % (i+1)] = F_FMT % rt
        results['sctso%dsd' % (i+1)] = F_FMT % sd
        if corr_f(resp_trial):
            so_cor += 1
    results['sctsotc'] = D_FMT % so_cor
    
    # overall
    results['sctoc'] = D_FMT % (so_cor + ss_cor)
            
    return results
