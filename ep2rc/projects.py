#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os
from . import io
from . import errors

import numpy as np

from pdb import set_trace

F_FMT = '%.3f'
FZ_FMT = '%0.3f'
D_FMT = '%d'

""" TASK PARSING FUNCTIONS """

def NF_REP(fobj, new_fname=None):
    """ This parses NFRO1 REP e-prime files """
    REP_DICT = {'fine': 'A', 'hope': 'A', 'kept': 'A', 'jeet': 'Non', 'libe': 'Non',
                'pait': 'Non', 'rock': 'C', 'ship': 'C', 'sit': 'C', 'pdgp': 'CS',
                'wlr': 'CS', 'fxct': 'CS', 'sound': 'C', 'wife': 'C', 'wood': 'C',
                'write': 'C', 'preet': 'Non', 'reat': 'Non', 'saip': 'Non', 'dwql': 'CS',
                'chdncp': 'CS', 'flhhr': 'CS', 'stop': 'A', 'try': 'A', 'turn': 'A',
                'buy': 'A', 'care': 'A', 'feel': 'A', 'brong': 'Non', 'doil': 'Non',
                'fomp': 'Non', 'box': 'C', 'dark': 'C', 'eat': 'C', 'farm': 'C',
                'yad': 'Non', 'spt': 'CS', 'rcd': 'CS', 'zood': 'Non', 'wrong': 'A',
                'floor': 'C', 'foot': 'C', 'wait': 'A', 'trat': 'Non', 'kwpt': 'CS',
                'mdp': 'CS', 'green': 'C', 'horse': 'C', 'hot': 'C', 'late': 'A',
                'rest': 'A', 'stay': 'A', 'skib': 'Non', 'smy': 'Non', 'tey': 'Non',
                'bhx': 'CS','hdrsp': 'CS','rzst': 'CS','line': 'C','moon': 'C','rain': 'C',
                'stnm': 'CS','sthnr': 'CS','hct': 'CS','wish': 'A','red': 'C','road': 'C',
                'gorn': 'Non','heen': 'Non','hoad': 'Non','svnt': 'CS','mlxth': 'CS','rock': 'C',
                'ship': 'C','sit': 'C','buy': 'A','care': 'A','feel': 'A','brong': 'Non',
                'doil': 'Non','fomp': 'Non','dwql': 'CS','chdncp': 'CS','flhhr': 'CS','stop': 'A',
                'try': 'A','turn': 'A','sound': 'C','wife': 'C','wood': 'C','write': 'C',
                'preet': 'Non','reat': 'Non','saip': 'Non','yad': 'Non','spt': 'CS','rcd': 'CS',
                'zood': 'Non','wrong': 'A','floor': 'C','foot': 'C','wait': 'A','trat': 'Non',
                'kwpt': 'CS','mdp': 'CS','box': 'C','dark': 'C','eat': 'C','farm': 'C',
                'line': 'C','moon': 'C','rain': 'C','stnm': 'CS','sthnr': 'CS','hct': 'CS',
                'wish': 'A','red': 'C','road': 'C','skib': 'Non','smy': 'Non','tey': 'Non',
                'bhx': 'CS','hdrsp': 'CS','rzst': 'CS','jeet': 'Non','libe': 'Non','pait': 'Non',
                'pdgp': 'CS','wlr': 'CS','fxct': 'CS','fine': 'A','hope': 'A','kept': 'A',
                'green': 'C','horse': 'C','hot': 'C','gorn': 'Non','heen': 'Non','hoad': 'Non',
                'svnt': 'CS','mlxth': 'CS','late': 'A','rest': 'A','stay': 'A','brong': 'Non','doil': 'Non',
                'fomp': 'Non','dwql': 'CS','chdncp': 'CS','flhhr': 'CS','wrong': 'A','floor': 'C',
                'foot': 'C','wait': 'A','trat': 'Non','kwpt': 'CS','mdp': 'CS','box': 'C',
                'dark': 'C','eat': 'C','preet': 'Non','reat': 'Non','saip': 'Non','stop': 'A',
                'try': 'A','turn': 'A','sound': 'C','wife': 'C','wood': 'C','write': 'C',
                'yad': 'Non','spt': 'CS','rcd': 'CS','zood': 'Non','rock': 'C','ship': 'C',
                'sit': 'C','buy': 'A','care': 'A','feel': 'A','stnm': 'CS','sthnr': 'CS',
                'hct': 'CS','wish': 'A','red': 'C','road': 'C','pait': 'Non','pdgp': 'CS','wlr': 'CS',
                'fxct': 'CS','fine': 'A','hope': 'A','kept': 'A','green': 'C','horse': 'C','hot': 'C',
                'gorn': 'Non','heen': 'Non','hoad': 'Non','svnt': 'CS','mlxth': 'CS','late': 'A','rest': 'A',
                'stay': 'A','hdrsp': 'CS','rzst': 'CS','jeet': 'Non','libe': 'Non','farm': 'C',
                'line': 'C','moon': 'C','rain': 'C','skib': 'Non','smy': 'Non','tey': 'Non','bhx': 'CS'}
    dl = io.split_dict(fobj, new_fname)

    try:
        m1_trials = [x for x in dl if x['M1'] != '.']
        m2_trials = [x for x in dl if x['M2'] != '.']
        m3_trials = [x for x in dl if x['M3'] != '.']
    except KeyError:
        raise errors.BadDataError()
    
    results = {}
    for m_data, m in zip((m1_trials, m2_trials, m3_trials), ('m1', 'm2', 'm3')):
        if m_data:
            #  text1 contains strings.  REP_DICT matches these strings to their 
            #  category.
            loop_data = zip(('A', 'C', 'Non', 'CS'),
                            (('6','1'), ('6','1'), ('5','2'), ('5','2')),
                            (('5','2'), ('5','2'), ('6','1'), ('6','1')),
                            ('abs', 'conc', 'non', 'cons'))
            for cat, good, bad, catt in loop_data:
                try:
                    trials = filter(lambda x: REP_DICT[x['text1']] == cat, m_data)
                    corr = filter(lambda x: x['stim.RESP'] in good, trials)
                    #  Accuracy = # of correct / # of trials * 100
                    acc = (float(len(corr)) / len(trials)) * 100
                    results['%s_%s_acc' % (m, catt)] = F_FMT % acc
                    #  binary vector to compute SD
                    resp = (1,) * len(corr) + (0,) * (len(trials) - len(corr))
                    accsd = np.std(np.array(resp))
                    results['%s_%s_accsd' % (m, catt)] = FZ_FMT % accsd
                    
                    #  Grab correct RT
                    corr_rt = np.array([float(t['stim.RT']) for t in corr])
                    #  Mean RT
                    rtavg = np.mean(corr_rt)
                    results['%s_%s_rtavg' % (m, catt)] = F_FMT % rtavg
                    #  SD of RT
                    rtsd = np.std(corr_rt)
                    results['%s_%s_rtsd' % (m, catt)] = FZ_FMT % rtsd
                    
                    #  N omit, comit
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good+bad, trials))
                    results['%s_%s_omit' % (m, catt)] = D_FMT % n_omit
                    n_comit = len(filter(lambda x: x['stim.RESP'] in bad, trials))
                    results['%s_%s_comit' % (m, catt)] = D_FMT % n_comit
                except ZeroDivisionError:
                    pass

    return results

def NF_MI(fobj, new_fname=None):
    """ This parses NFRO1 MI e prime files"""
    dl = io.split_dict(fobj, new_fname)

    dl[:] = [x for x in dl if x['runList'] != 'pract']
    
    try:
        m1_trials = [x for x in dl if x['Image'] != '.']
        m2_trials = [x for x in dl if x['Image2'] != '.']
    except KeyError:
        raise errors.BadDataError()
        
    results = {}    

    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        if m_data:
            #  text2 contains strings like H10.bmp
            #  S*.bmp are not-filled in, thus requiring actual work
            #  So the real trials are x['text2'][0] == 'S'
            #  Fake trials are others
            real_trials = filter(lambda x: x['text2'][0] == 'S', m_data)
            cont_trials = filter(lambda x: x['text2'][0] != 'S', m_data)
    
            #  Responses are correct if the x was in the letter (a '1' the correct column) and the response was '6'
            #  OR the x wasn't in the letter ('2' in the correct) and the response was '5'
            corrf = lambda x: ((x['correct'] == '1' and x['Target.RESP'] in ('6','1')) or (x['correct'] == '2' and x['Target.RESP'] == '5'))
            #  A false positive is a positive response when the x wasn't in the letter
            fpf = lambda x: x['correct'] == '2' and x['Target.RESP'] in ('6','1')
            #  A false negative is a negative response when the x was in the letter
            fnf = lambda x: x['correct'] == '1' and x['Target.RESP'] in ('5','2')
            omitf = lambda x: x['Target.RESP'] not in ('5', '6', '1', '2')
            for tdata, ttext in zip((real_trials, cont_trials),('imag', 'cont')):
                try:
                    #  Use the correct function
                    corr = [x for x in tdata if corrf(x)]
                    #  Use the false positive function
                    fp = [x for x in tdata if fpf(x)]
                    results['%s_%s_fp' % (m, ttext)] = D_FMT % len(fp)
                    #  Use the false negative function
                    fn = [x for x in tdata if fnf(x)]
                    results['%s_%s_fn' % (m, ttext)] = D_FMT % len(fn)
                    #  Use omit function
                    omit = [x for x in tdata if omitf(x)]
                    results['%s_%s_omit' % (m, ttext)] = D_FMT % len(omit)
                    
                    acc = (float(len(corr)) / len(tdata)) * 100
                    results['%s_%s_acc' % (m, ttext)] = F_FMT % acc
                    #  Generate a binary vector
                    resp = (1,) * len(corr) + (0,) * (len(tdata) - len(corr))
                    accsd = np.std(np.array(resp))
                    results['%s_%s_accsd' % (m, ttext)] = FZ_FMT % accsd
        
                    all_rt = np.array([float(x['Target.RT']) for x in corr])
                    rt_avg = np.mean(all_rt)
                    results['%s_%s_rtavg' % (m, ttext)] = F_FMT % rt_avg
                    rt_sd = np.std(all_rt)
                    results['%s_%s_rtsd' % (m, ttext)] = FZ_FMT % rt_sd
                except ZeroDivisionError:
                    pass
    return results

def NF_SWR(fobj, new_fname=None):
    """ This parses NFRO1 SWR e-prime files"""
    dl = io.split_dict(fobj, new_fname)

    #  Remove the practice trial
    dl[:] = [x for x in dl if x['List3.Sample'] != '.']

    try:
        m1_trials = [x for x in dl if int(x['List3.Sample']) < 51]
        m2_trials = [x for x in dl if int(x['List3.Sample']) > 50]
    except KeyError:
        raise errors.BadDataError()
        
    res = {}
    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        if m_data:
            loop_data = zip(('HAI', 'HAR', 'HCI', 'HCR', 'word', 'nonword'),
                            ('category',) * 4 + ('type',) * 2,
                            (('6','1'), ('6','1'), ('6','1'), ('6','1'), ('6','1'), ('5','2')),
                            (('5','2'), ('5','2'), ('5','2'), ('5','2'), ('5','2'), ('6','1')))
            for cat, cat_key, good, bad in loop_data:
                try:
                    trials = filter(lambda x: x[cat_key] == cat, m_data)
                    corr = filter(lambda x: x['stim.RESP'] in good, trials)
                    #  Accuracy = # of correct / # of trials * 100
                    acc = (float(len(corr)) / len(trials)) * 100
                    res['%s_%s_acc' % (m, cat.lower())] = F_FMT % acc
                    #  make a binary vector to compute std deviation
                    resp = (1,) * len(corr) + (0,) * (len(trials) - len(corr))
                    acc_std = np.std(np.array(resp))
                    res['%s_%s_accsd' % (m, cat.lower())] = FZ_FMT % acc_std
        
                    #  Grab all correct reaction times
                    all_rt = np.array([float(t['stim.RT']) for t in corr])
                    #  Mean of reaction time
                    rt_avg = np.mean(all_rt)
                    res['%s_%s_rtavg' % (m, cat.lower())] = F_FMT % rt_avg 
                    #  STD of reaction time
                    rt_std = np.std(all_rt)
                    res['%s_%s_rtsd' % (m, cat.lower())] =  FZ_FMT % rt_std
        
                    #  N omit/comit
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good+bad, trials))
                    res['%s_%s_omit' % (m, cat.lower())] = D_FMT % n_omit
                    n_comit = len(filter(lambda x: x['stim.RESP'] in bad, trials))
                    res['%s_%s_comit' % (m, cat.lower())] = D_FMT % n_comit
                except ZeroDivisionError:
                    pass
    return res

def NF_PIC(fobj, new_fname=None):
    """ This parses NFRO1 PIC e-prime files"""
    dl = io.split_dict(fobj, new_fname)

    try:
        m1_trials = filter(lambda x: x['M1'] != '.', dl)
        m2_trials = filter(lambda x: x['M2'] != '.', dl)
    except KeyError:
        raise errors.BadDataError()
    
    res = {}

    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        if m_data:
            loop_data = zip(('psw', 'con', 'wrd', 'match'),
                            (('5','2'), ('5','2'), ('5','2'), ('6','1')),
                            (('6','1'), ('6','1'), ('6','1'), ('5','2')))
            for typ, good, bad in loop_data:
                try:
                    trials = filter(lambda x: x['type'] == typ, m_data)
                    correct = filter(lambda x: x['stim.RESP'] in good, trials)
                    #  Accuracy = # of correct / # trials * 100
                    acc = (float(len(correct)) / len(trials)) * 100
                    res['%s_%s_acc' % (m, typ)] = F_FMT % acc
        
                    #  Make a binary vector to compute sd
                    resp = (1,) * len(correct) + (0,) * (len(trials) - len(correct))
                    acc_std = np.std(np.array(resp))
                    res['%s_%s_accsd' % (m, typ)] = FZ_FMT % acc_std
        
                    #  Grab the correct reaction times
                    all_rt = np.array([float(t['stim.RT']) for t in correct])
        
                    #  Mean of correct rt
                    rt_avg = np.mean(all_rt)
                    res['%s_%s_rtavg' % (m, typ)] = F_FMT % rt_avg
                    #  SD of reaction time
                    rt_std = np.std(all_rt)
                    res['%s_%s_rtsd' % (m, typ)] = FZ_FMT % rt_std
        
                    #  N omit/comit
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good + bad, trials))
                    res['%s_%s_omit' % (m, typ)] = D_FMT % n_omit
                    n_comit = len(filter(lambda x: x['stim.RESP'] in bad, trials))
                    res['%s_%s_comit' % (m, typ)] = D_FMT % n_comit
                except ZeroDivisionError:
                    pass
    return res

def NFB_MR(fobj, new_fname):
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
    
def NFB_MI(fobj, new_fname):
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

def NFB_OLSON(fobj, new_fname):
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

def NFB_FIG(fobj, new_fname):
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

def NFB_SENT(fobj, new_fname):
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

class BaseProject(object):
    """ Base class from which all Projects should inherit"""
    
    def __init__(self, fname, fobj, database='in-magnet'):
        """ Constructor """
        #  Required info
        self.fname = fname
        self.fobj = fobj
        self.database = database
        
        self.project = None
        self.behavid = None
        self.task = None
        
        self.parse_fname()

    def split_fname(self):
        bname = os.path.basename(self.fname)
        self.bname = bname
        name, ext = os.path.splitext(bname)
        parts = name.split('_')
        try:
            self.project = parts[0]
            self.task = parts[1]
            self.behavid = parts[2]
            self.scanid = parts[3]
        except IndexError:
            raise ValueError("Poorly named file :(")
        return parts
        
    def parse_fname(self):
        """ PRIVATE Populate information from file name """
        raise NotImplementedError

    def rc_prefix(self):
        """ PRIVATE Return prefix (mostly used for projects that go to in-magnet """
        pass
        
    def key_map(self):
        """ PRIVATE Return a function transforming raw keys to RC fields """
        pass
        
    def new_fname(self):
        """ PRIVATE Return the path to where the copy should go """
        pass
        
    def parse(self, fname, fobj):
        """ Parse the file and return redcap-able results """
        raise NotImplementedError

    def upload_key(self):
        """ Returns a key for the in-magnet database that can be used to check 
        for previous uploads """
        return None
        
class NF(BaseProject):
    
    def __init__(self, fname, fobj, database='in-magnet'):
        super(NF, self).__init__(fname, fobj, database)    
        self.rcmap = {'SWR': 'swr1', 'MI': 'mi1', 'REP': 'rep1', 'PIC': 'pic1'}
        self.parse_fname()

    def parse_fname(self):
        parts = self.split_fname()
        if self.task in ('SWR', 'PIC', 'MI'):
            #  GRANT_TASK_BEHAVID_SCANID_VISIT
            self.visit = parts[4]
        if self.task in ('SWR', 'PIC'):
            #  GRANT_TASK_BEHAVID_SCANID_VISIT_LIST
            self.list = parts[5]
    
    def parse(self):
        tasks = {'SWR': NF_SWR, 'MI': NF_MI, 'REP': NF_REP, 'PIC': NF_PIC}
        func = tasks[self.task]
        data = func(self.fobj, self.copy_fname())
        #  define a mapping from keys in data to keys we can upload
        key_map = self.key_map()
        to_redcap = {}
        if not data:
            raise ValueError("Parsed nothing from this file :(")
        for k,v in data.items():
            to_redcap[key_map(k)] = v
        #  Branch based on which database we're going to_redcap
        if self.database == 'in-magnet':
            to_redcap['grant'] = self.project
            to_redcap['id'] = '%s_%s' % (self.behavid, self.scanid)
            #  Fill out upload field
            to_redcap[key_map('upload')] = 'yes'
        elif self.database == 'NF':
            to_redcap['id'] = self.behavid
        return to_redcap

    def key_map(self):
        if self.task == 'REP':
            f = lambda x: 'rep1_%s' % x
        else:
            f = lambda x: '%s_%s_%s' % (self.rcmap[self.task], self.visit.lower(), x)
        return f
        
    def copy_fname(self):
        _platform = os.uname()[0]
        if _platform == 'Linux':
            prefix = os.path.join('/', 'fs0')
        else:
            prefix = os.path.join(os.path.expanduser('~'), 'Code', 'eprime2redcap')
        new_dir = os.path.join(prefix, 'New_Server', 'NF',
                'In_Behavioral', '_'.join([self.behavid, self.scanid]))
        # Make dirs if necessary
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)
        return os.path.join(new_dir, self.bname+'.txt')
     
    def upload_key(self):
        key = None
        if self.database == 'in-magnet':
            if self.task in ('SWR', 'PIC', 'MI'):
                key = '%s_%s_upload' % (self.rcmap[self.task], self.visit.lower())
            elif self.task == 'REP':
                key = '%s_upload' % self.rcmap[self.task]
        return key
        
class NFB(BaseProject):
    
    def copy_fname(self):
        _platform = os.uname()[0]
        if _platform == 'Linux':
            prefix = os.path.join('/', 'fs0')
        else:
            prefix = os.path.join(os.path.expanduser('~'), 'Code', 'eprime2redcap')
        new_dir = os.path.join(prefix, 'New_Server', 'NF', 
                'Out_Behavioral', '_'.join([self.behavid, self.scanid]))
        # Make dirs if necessary
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)
        return os.path.join(new_dir, self.bname+'.txt')

    def parse_fname(self):
        parts = self.split_fname()
        try:
            if self.task in ('FIG', 'MI', 'MR', 'OLSON'):
                self.visit = parts[4]
        except IndexError:
            raise ValueError("Poorly named file :(")
    
    def parse(self):
        tasks = {'OLSON': NFB_OLSON, 'MI': NFB_MI, 'MR': NFB_MR, 'SENT': NFB_SENT,
                    'FIG': NFB_FIG}
        func = tasks[self.task]
        data = func(self.fobj, self.copy_fname())
        if hasattr(self, 'visit'):
            if self.visit == 'Pre':
                visit = '1'
            else:
                visit = '2'
            key_map = lambda x: x.replace('X', visit)
        else:
            key_map = lambda x: x
        if not data: 
            raise ValueError("Parsed nothing from this file :(")
        to_redcap = {}
        for k,v in data.items():
            to_redcap[key_map(k)] = v
        #  These data will only ever go to the NF database
        to_redcap['studyid'] = self.behavid
        return to_redcap