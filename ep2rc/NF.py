#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import sys
import os
import numpy as np

from . import errors
from . import io

F_FMT = '%.3f'
FZ_FMT = '%0.3f'
D_FMT = '%d'

REP_DICT = {
'fine': 'A',
'hope': 'A',
'kept': 'A',
'jeet': 'Non',
'libe': 'Non',
'pait': 'Non',
'rock': 'C',
'ship': 'C',
'sit': 'C',
'pdgp': 'CS',
'wlr': 'CS',
'fxct': 'CS',
'sound': 'C',
'wife': 'C',
'wood': 'C',
'write': 'C',
'preet': 'Non',
'reat': 'Non',
'saip': 'Non',
'dwql': 'CS',
'chdncp': 'CS',
'flhhr': 'CS',
'stop': 'A',
'try': 'A',
'turn': 'A',
'buy': 'A',
'care': 'A',
'feel': 'A',
'brong': 'Non',
'doil': 'Non',
'fomp': 'Non',
'box': 'C',
'dark': 'C',
'eat': 'C',
'farm': 'C',
'yad': 'Non',
'spt': 'CS',
'rcd': 'CS',
'zood': 'Non',
'wrong': 'A',
'floor': 'C',
'foot': 'C',
'wait': 'A',
'trat': 'Non',
'kwpt': 'CS',
'mdp': 'CS',
'green': 'C',
'horse': 'C',
'hot': 'C',
'late': 'A',
'rest': 'A',
'stay': 'A',
'skib': 'Non',
'smy': 'Non',
'tey': 'Non',
'bhx': 'CS',
'hdrsp': 'CS',
'rzst': 'CS',
'line': 'C',
'moon': 'C',
'rain': 'C',
'stnm': 'CS',
'sthnr': 'CS',
'hct': 'CS',
'wish': 'A',
'red': 'C',
'road': 'C',
'gorn': 'Non',
'heen': 'Non',
'hoad': 'Non',
'svnt': 'CS',
'mlxth': 'CS',
'rock': 'C',
'ship': 'C',
'sit': 'C',
'buy': 'A',
'care': 'A',
'feel': 'A',
'brong': 'Non',
'doil': 'Non',
'fomp': 'Non',
'dwql': 'CS',
'chdncp': 'CS',
'flhhr': 'CS',
'stop': 'A',
'try': 'A',
'turn': 'A',
'sound': 'C',
'wife': 'C',
'wood': 'C',
'write': 'C',
'preet': 'Non',
'reat': 'Non',
'saip': 'Non',
'yad': 'Non',
'spt': 'CS',
'rcd': 'CS',
'zood': 'Non',
'wrong': 'A',
'floor': 'C',
'foot': 'C',
'wait': 'A',
'trat': 'Non',
'kwpt': 'CS',
'mdp': 'CS',
'box': 'C',
'dark': 'C',
'eat': 'C',
'farm': 'C',
'line': 'C',
'moon': 'C',
'rain': 'C',
'stnm': 'CS',
'sthnr': 'CS',
'hct': 'CS',
'wish': 'A',
'red': 'C',
'road': 'C',
'skib': 'Non',
'smy': 'Non',
'tey': 'Non',
'bhx': 'CS',
'hdrsp': 'CS',
'rzst': 'CS',
'jeet': 'Non',
'libe': 'Non',
'pait': 'Non',
'pdgp': 'CS',
'wlr': 'CS',
'fxct': 'CS',
'fine': 'A',
'hope': 'A',
'kept': 'A',
'green': 'C',
'horse': 'C',
'hot': 'C',
'gorn': 'Non',
'heen': 'Non',
'hoad': 'Non',
'svnt': 'CS',
'mlxth': 'CS',
'late': 'A',
'rest': 'A',
'stay': 'A',
'brong': 'Non',
'doil': 'Non',
'fomp': 'Non',
'dwql': 'CS',
'chdncp': 'CS',
'flhhr': 'CS',
'wrong': 'A',
'floor': 'C',
'foot': 'C',
'wait': 'A',
'trat': 'Non',
'kwpt': 'CS',
'mdp': 'CS',
'box': 'C',
'dark': 'C',
'eat': 'C',
'preet': 'Non',
'reat': 'Non',
'saip': 'Non',
'stop': 'A',
'try': 'A',
'turn': 'A',
'sound': 'C',
'wife': 'C',
'wood': 'C',
'write': 'C',
'yad': 'Non',
'spt': 'CS',
'rcd': 'CS',
'zood': 'Non',
'rock': 'C',
'ship': 'C',
'sit': 'C',
'buy': 'A',
'care': 'A',
'feel': 'A',
'stnm': 'CS',
'sthnr': 'CS',
'hct': 'CS',
'wish': 'A',
'red': 'C',
'road': 'C',
'pait': 'Non',
'pdgp': 'CS',
'wlr': 'CS',
'fxct': 'CS',
'fine': 'A',
'hope': 'A',
'kept': 'A',
'green': 'C',
'horse': 'C',
'hot': 'C',
'gorn': 'Non',
'heen': 'Non',
'hoad': 'Non',
'svnt': 'CS',
'mlxth': 'CS',
'late': 'A',
'rest': 'A',
'stay': 'A',
'hdrsp': 'CS',
'rzst': 'CS',
'jeet': 'Non',
'libe': 'Non',
'farm': 'C',
'line': 'C',
'moon': 'C',
'rain': 'C',
'skib': 'Non',
'smy': 'Non',
'tey': 'Non',
'bhx': 'CS'}


def REP(fobj, new_fname=None):
    """ This parses NFRO1 REP e-prime files """
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

def MI(fobj, new_fname=None):
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

def PIC(fobj, new_fname=None):
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

def SWR(fobj, new_fname=None):
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

if __name__ == '__main__':
    swr = open(os.path.expanduser('/Volumes/erbrainlab/Team Drive/Individual Folders/Sarah R/NF Rename Task/All/NF_SWR_74_3020_Pre_ListA.txt'))
    swr_data = SWR(swr)
    swr.close()
    print
    print

    pic = open(os.path.expanduser('/Volumes/erbrainlab/Team Drive/Individual Folders/Sarah R/NF Rename Task/All/NF_PIC_63_2020_Post_ListA.txt'))
    pic_data = PIC(pic)
    pic.close()

    print
    print

    mi = open(os.path.expanduser('/Volumes/erbrainlab/Team Drive/Individual Folders/Sarah R/NF Rename Task/All/NF_MI_68_3018_Post.txt'))
    mi_data = MI(mi)
    mi.close()
    print
    print

    rep = open(os.path.expanduser('~/Desktop/EPRIME/REP/NF_REP_Test_Test.txt'))
    rep_data = REP(rep)
    rep.close()
