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
    dl = io.split_dict(fobj, new_fname=None)

    if len(dl) != 216:
        raise errors.BadDataError("Did not find 216 trials in this REP e-prime file :(")
    
    m1_trials = dl[:72]
    m2_trials = dl[72:144]
    m3_trials = dl[144:]
    
    results = {}
    for m_data, m in zip((m1_trials, m2_trials, m3_trials), ('m1', 'm2', 'm3')):
        #  text1 contains strings.  REP_DICT matches these strings to their 
        #  category.
        loop_data = zip(('A', 'C', 'Non', 'CS'),
                        ('6', '6', '5', '5'),
                        ('5', '5', '6', '6'),
                        ('abs', 'conc', 'non', 'cons'))
        for cat, good, bad, catt in loop_data:
            trials = filter(lambda x: REP_DICT[x['text1']] == cat, m_data)
            corr = filter(lambda x: x['stim.RESP'] == good, trials)
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
            n_omit = len(filter(lambda x: x['stim.RESP'] not in (good, bad), trials))
            results['%s_%s_omit' % (m, catt)] = D_FMT % n_omit
            n_comit = len(filter(lambda x: x['stim.RESP'] == bad, trials))
            results['%s_%s_comit' % (m, catt)] = D_FMT % n_comit
    return results

def MI(fobj, new_fname=None):
    """ This parses NFRO1 MI e prime files"""
    dl = io.split_dict(fobj, new_fname=None)

    #  No filter needed

    if len(dl) != 96:
        raise errors.BadDataError("Did not find 96 trials in this MI e-primee file :(")

    m1_trials = dl[:48]
    m2_trials = dl[48:]   
    
    results = {}    

    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        #  text2 contains strings like H10.bmp
        #  S*.bmp are not-filled in, thus requiring actual work
        #  So the real trials are x['text2'][0] == 'S'
        #  Fake trials are others
        real_trials = filter(lambda x: x['text2'][0] == 'S', m_data)
        cont_trials = filter(lambda x: x['text2'][0] != 'S', m_data)

        #  Responses are correct if the x was in the letter (a '1' the correct column) and the response was '6'
        #  OR the x wasn't in the letter ('2' in the correct) and the response was '5'
        corrf = lambda x: ((x['correct'] == '1' and x['Target.RESP'] == '6') or (x['correct'] == '2' and x['Target.RESP'] == '5'))
        #  A false positive is a positive response when the x wasn't in the letter
        fpf = lambda x: x['correct'] == '2' and x['Target.RESP'] == '6'
        #  A false negative is a negative response when the x was in the letter
        fnf = lambda x: x['correct'] == '1' and x['Target.RESP'] == '5'
        omitf = lambda x: x['Target.RESP'] not in ('5', '6')
        for tdata, ttext in zip((real_trials, cont_trials),('imag', 'cont')):
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
    return results

def PIC(fobj, new_fname=None):
    """ This parses NFRO1 PIC e-prime files"""
    dl = io.split_dict(fobj, new_fname=None)

    #  Remove practice trial
    dl[:] = [x for x in dl if x['runList'] != 'PracList']

    #  If we don't have 134 trials, uh oh!
    if len(dl) != 188:
        raise errors.BadDataError("Did not find 188 trials in this PIC e-prime file :(")

    m1_trials = dl[:94]
    m2_trials = dl[94:]
    res = {}

    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        loop_data = zip(('psw', 'con', 'wrd', 'match'),
                        ('5', '5', '5', '6'),
                        ('6', '6', '6', '5'))
        for typ, good, bad in loop_data:
            trials = filter(lambda x: x['type'] == typ, m_data)
            correct = filter(lambda x: x['stim.RESP'] == good, trials)
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
            n_omit = len(filter(lambda x: x['stim.RESP'] not in (good, bad), trials))
            res['%s_%s_omit' % (m, typ)] = D_FMT % n_omit
            n_comit = len(filter(lambda x: x['stim.RESP'] == bad, trials))
            res['%s_%s_comit' % (m, typ)] = D_FMT % n_comit
    return res

def SWR(fobj, new_fname=None):
    """ This parses NFRO1 SWR e-prime files"""
    dl = io.split_dict(fobj, new_fname=None)

    #  Remove the practice trial
    dl[:] = [x for x in dl if x['runList'] != 'PracList']

    #  If we don't have 100 trials, uh oh!
    if len(dl) != 100:
        raise errors.BadDataError("Did not find 100 trials in this SWR e-prime file :(")

    m1_trials = dl[:50]
    m2_trials = dl[50:]
    res = {}
    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        loop_data = zip(('HAI', 'HAR', 'HCI', 'HCR', 'word', 'nonword'),
                        ('category',) * 4 + ('type',) * 2,
                        ('6', '6', '6', '6', '6', '5'),
                        ('5', '5', '5', '5', '5', '6'))
        for cat, cat_key, good, bad in loop_data:
            trials = filter(lambda x: x[cat_key] == cat, m_data)
            corr = filter(lambda x: x['stim.RESP'] == good, trials)
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
            n_omit = len(filter(lambda x: x['stim.RESP'] not in (good, bad), trials))
            res['%s_%s_omit' % (m, cat.lower())] = D_FMT % n_omit
            n_comit = len(filter(lambda x: x['stim.RESP'] == bad, trials))
            res['%s_%s_comit' % (m, cat.lower())] = D_FMT % n_comit
    return res

if __name__ == '__main__':
    swr = open(os.path.expanduser('~/Desktop/EPRIME/SWR/NF_SWR_Test_Test_Pre_ListA.txt'))
    swr_data = SWR(swr)
    swr.close()
    print
    print

    pic = open(os.path.expanduser('~/Desktop/EPRIME/PIC/NF_PIC_Test_Test_Post_ListA.txt'))
    pic_data = PIC(pic)
    pic.close()

    print
    print

    mi = open(os.path.expanduser('~/Desktop/EPRIME/MI/NF_MI_Test_Test_Pre.txt'))
    mi_data = MI(mi)
    mi.close()
    print
    print

    rep = open(os.path.expanduser('~/Desktop/EPRIME/REP/NF_REP_Test_Test.txt'))
    rep_data = REP(rep)
    rep.close()
