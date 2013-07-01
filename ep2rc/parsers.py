#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import numpy as np


from . import io
from . import errors

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
                'bhx': 'CS', 'hdrsp': 'CS', 'rzst': 'CS', 'line': 'C', 'moon': 'C', 'rain': 'C',
                'stnm': 'CS', 'sthnr': 'CS', 'hct': 'CS', 'wish': 'A', 'red': 'C', 'road': 'C',
                'gorn': 'Non', 'heen': 'Non', 'hoad': 'Non', 'svnt': 'CS', 'mlxth': 'CS', 'rock': 'C',
                'ship': 'C', 'sit': 'C', 'buy': 'A', 'care': 'A', 'feel': 'A', 'brong': 'Non',
                'doil': 'Non', 'fomp': 'Non', 'dwql': 'CS', 'chdncp': 'CS', 'flhhr': 'CS', 'stop': 'A',
                'try': 'A', 'turn': 'A', 'sound': 'C', 'wife': 'C', 'wood': 'C', 'write': 'C',
                'preet': 'Non', 'reat': 'Non', 'saip': 'Non', 'yad': 'Non', 'spt': 'CS', 'rcd': 'CS',
                'zood': 'Non', 'wrong': 'A', 'floor': 'C', 'foot': 'C', 'wait': 'A', 'trat': 'Non',
                'kwpt': 'CS', 'mdp': 'CS', 'box': 'C', 'dark': 'C', 'eat': 'C', 'farm': 'C',
                'line': 'C', 'moon': 'C', 'rain': 'C', 'stnm': 'CS', 'sthnr': 'CS', 'hct': 'CS',
                'wish': 'A', 'red': 'C', 'road': 'C', 'skib': 'Non', 'smy': 'Non', 'tey': 'Non',
                'bhx': 'CS', 'hdrsp': 'CS', 'rzst': 'CS', 'jeet': 'Non', 'libe': 'Non', 'pait': 'Non',
                'pdgp': 'CS', 'wlr': 'CS', 'fxct': 'CS', 'fine': 'A', 'hope': 'A', 'kept': 'A',
                'green': 'C', 'horse': 'C', 'hot': 'C', 'gorn': 'Non', 'heen': 'Non', 'hoad': 'Non',
                'svnt': 'CS', 'mlxth': 'CS', 'late': 'A', 'rest': 'A', 'stay': 'A', 'brong': 'Non', 'doil': 'Non',
                'fomp': 'Non', 'dwql': 'CS', 'chdncp': 'CS', 'flhhr': 'CS', 'wrong': 'A', 'floor': 'C',
                'foot': 'C', 'wait': 'A', 'trat': 'Non', 'kwpt': 'CS', 'mdp': 'CS', 'box': 'C',
                'dark': 'C', 'eat': 'C', 'preet': 'Non', 'reat': 'Non', 'saip': 'Non', 'stop': 'A',
                'try': 'A', 'turn': 'A', 'sound': 'C', 'wife': 'C', 'wood': 'C', 'write': 'C',
                'yad': 'Non', 'spt': 'CS', 'rcd': 'CS', 'zood': 'Non', 'rock': 'C', 'ship': 'C',
                'sit': 'C', 'buy': 'A', 'care': 'A', 'feel': 'A', 'stnm': 'CS', 'sthnr': 'CS',
                'hct': 'CS', 'wish': 'A', 'red': 'C', 'road': 'C', 'pait': 'Non', 'pdgp': 'CS', 'wlr': 'CS',
                'fxct': 'CS', 'fine': 'A', 'hope': 'A', 'kept': 'A', 'green': 'C', 'horse': 'C', 'hot': 'C',
                'gorn': 'Non', 'heen': 'Non', 'hoad': 'Non', 'svnt': 'CS', 'mlxth': 'CS', 'late': 'A', 'rest': 'A',
                'stay': 'A', 'hdrsp': 'CS', 'rzst': 'CS', 'jeet': 'Non', 'libe': 'Non', 'farm': 'C',
                'line': 'C', 'moon': 'C', 'rain': 'C', 'skib': 'Non', 'smy': 'Non', 'tey': 'Non', 'bhx': 'CS'}
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
                            (('6', '1'), ('6', '1'), ('5', '2'), ('5', '2')),
                            (('5', '2'), ('5', '2'), ('6', '1'), ('6', '1')),
                            ('abs', 'conc', 'non', 'cons'))
            for cat, good, bad, catt in loop_data:
                try:
                    trials = filter(lambda x: REP_DICT[x['text1']] == cat, m_data)
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good+bad, trials))
                    results['%s_%s_omit' % (m, catt)] = D_FMT % n_omit
                    #  We need to remove omitted trials from trials we peform stats on
                    trials[:] = filter(lambda x: REP_DICT[x['text1']] == cat and x['stim.RESP'] in good+bad, trials)
                    # Now we can proceed
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

                    #  comit
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
            corrf = lambda x: ((x['correct'] == '1' and x['Target.RESP'] in ('6', '1')) or (x['correct'] == '2' and x['Target.RESP'] == '5'))
            #  A false positive is a positive response when the x wasn't in the letter
            fpf = lambda x: x['correct'] == '2' and x['Target.RESP'] in ('6', '1')
            #  A false negative is a negative response when the x was in the letter
            fnf = lambda x: x['correct'] == '1' and x['Target.RESP'] in ('5', '2')
            omitf = lambda x: x['Target.RESP'] not in ('5', '6', '1', '2')
            for tdata, ttext in zip((real_trials, cont_trials), ('imag', 'cont')):
                try:
                    #  Use omit function
                    omit = [x for x in tdata if omitf(x)]
                    results['%s_%s_omit' % (m, ttext)] = D_FMT % len(omit)
                    tdata_noomit = filter(lambda x: not omitf(x), tdata)
                    #  Use the correct function
                    corr = [x for x in tdata_noomit if corrf(x)]
                    #  Use the false positive function
                    fp = [x for x in tdata_noomit if fpf(x)]
                    results['%s_%s_fp' % (m, ttext)] = D_FMT % len(fp)
                    #  Use the false negative function
                    fn = [x for x in tdata_noomit if fnf(x)]
                    results['%s_%s_fn' % (m, ttext)] = D_FMT % len(fn)

                    acc = (float(len(corr)) / len(tdata)) * 100
                    results['%s_%s_acc' % (m, ttext)] = F_FMT % acc
                    #  Generate a binary vector
                    resp = (1,) * len(corr) + (0,) * (len(tdata_noomit) - len(corr))
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
    dl[:] = [x for x in dl if x['List3.Sample'] not in ('.', '')]

    try:
        m1_trials = [x for x in dl if int(x['List3.Sample']) < 51]
        m2_trials = [x for x in dl if int(x['List3.Sample']) > 50]
    except KeyError:
        raise errors.BadDataError()

    res = {}
    TP = 0  # True positives are Word correct
    TN = 0  # True negatives are Nonword correct
    FP = 0  # False positives are Word incorrect
    FN = 0  # False negatives are Nonword incorrect
    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        if m_data:
            loop_data = zip(('HAI', 'HAR', 'HCI', 'HCR', 'word', 'nonword'),
                            ('category',) * 4 + ('type',) * 2,
                            (('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('5', '2')),
                            (('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('6', '1')))
            for cat, cat_key, good, bad in loop_data:
                try:
                    trials = filter(lambda x: x[cat_key] == cat, m_data)
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good+bad, trials))
                    res['%s_%s_omit' % (m, cat.lower())] = D_FMT % n_omit
                    #  Remove omits from trials
                    trials[:] = filter(lambda x: x['stim.RESP'] in good+bad, trials)
                    corr = filter(lambda x: x['stim.RESP'] in good, trials)
                    if cat == 'word':
                        #  Add to TP
                        TP += len(corr)
                    elif cat == 'nonword':
                        #  Add to TN
                        TN += len(corr)
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
                    res['%s_%s_rtsd' % (m, cat.lower())] = FZ_FMT % rt_std

                    #  comit
                    n_comit = len(filter(lambda x: x['stim.RESP'] in bad, trials))
                    if cat == 'word':
                        #  Add to FP
                        FP += n_comit
                    elif cat == 'nonword':
                        FN += n_comit
                    res['%s_%s_comit' % (m, cat.lower())] = D_FMT % n_comit
                except ZeroDivisionError:
                    pass
    res['aprime'] = FZ_FMT % aprime(TP, TN, FP, FN)
    return res


def RCK_SWR(fobj, new_fname=None):
    """ This parses RCK SWR e-prime files"""
    dl = io.split_dict(fobj, new_fname)

    #  Remove the practice trial
    dl[:] = [x for x in dl if x['List3.Sample'] not in ('.', '')]

    try:
        m1_trials = [x for x in dl if int(x['List3.Sample']) < 51]
        m2_trials = [x for x in dl if 101 > int(x['List3.Sample']) > 50]
        m3_trials = [x for x in dl if 151 > int(x['List3.Sample']) > 100]
        m4_trials = [x for x in dl if int(x['List3.Sample']) > 150]
    except KeyError:
        raise errors.BadDataError()

    res = {}
    TP = 0  # True positives are Word correct
    TN = 0  # True negatives are Nonword correct
    FP = 0  # False positives are Word incorrect
    FN = 0  # False negatives are Nonword incorrect
    for m_data, m in zip((m1_trials, m2_trials, m3_trials, m4_trials), ('m1', 'm2', 'm3', 'm4')):
        if m_data:
            loop_data = zip(('HAI', 'HAR', 'HCI', 'HCR', 'LAI', 'LAR', 'LCI', 'LCR', 'word', 'nonword'),
                            ('category',) * 8 + ('type',) * 2,
                            (('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('6', '1'), ('5', '2')),
                            (('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('5', '2'), ('6', '1')))
            for cat, cat_key, good, bad in loop_data:
                try:
                    trials = filter(lambda x: x[cat_key] == cat, m_data)
                    if len(trials) == 0:
                        continue
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good+bad, trials))
                    res['%s_%s_omit' % (m, cat.lower())] = D_FMT % n_omit
                    #  Remove omits from trials
                    trials[:] = filter(lambda x: x['stim.RESP'] in good+bad, trials)
                    corr = filter(lambda x: x['stim.RESP'] in good, trials)
                    if cat == 'word':
                        #  Add to TP
                        TP += len(corr)
                    elif cat == 'nonword':
                        #  Add to TN
                        TN += len(corr)
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
                    res['%s_%s_rtsd' % (m, cat.lower())] = FZ_FMT % rt_std

                    #  comit
                    n_comit = len(filter(lambda x: x['stim.RESP'] in bad, trials))
                    if cat == 'word':
                        #  Add to FP
                        FP += n_comit
                    elif cat == 'nonword':
                        FN += n_comit
                    res['%s_%s_comit' % (m, cat.lower())] = D_FMT % n_comit
                except ZeroDivisionError:
                    pass
    res['aprime'] = FZ_FMT % aprime(TP, TN, FP, FN)
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
    TP = 0  # True positive Match Correct
    TN = 0  # True negative Nonmatch correct
    FP = 0  # False positive Match incorrect
    FN = 0  # False negative Nonmatch incorrect
    for m_data, m in zip((m1_trials, m2_trials), ('m1', 'm2')):
        if m_data:
            loop_data = zip(('psw', 'con', 'wrd', 'match'),
                            (('5', '2'), ('5', '2'), ('5', '2'), ('6', '1')),
                            (('6', '1'), ('6', '1'), ('6', '1'), ('5', '2')))
            for typ, good, bad in loop_data:
                try:
                    trials = filter(lambda x: x['type'] == typ, m_data)
                    n_omit = len(filter(lambda x: x['stim.RESP'] not in good + bad, trials))
                    res['%s_%s_omit' % (m, typ)] = D_FMT % n_omit
                    #  Remove omits from trials
                    trials[:] = filter(lambda x: x['stim.RESP'] in good + bad, trials)
                    correct = filter(lambda x: x['stim.RESP'] in good, trials)
                    if typ == 'match':
                        #  Add to TP
                        TP += len(correct)
                    else:
                        #  Add to TN
                        TN += len(correct)
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

                    #  comit
                    n_comit = len(filter(lambda x: x['stim.RESP'] in bad, trials))
                    if type == 'match':
                        #  Add to FP
                        FP += n_comit
                    else:
                        FP += n_comit
                    res['%s_%s_comit' % (m, typ)] = D_FMT % n_comit
                except ZeroDivisionError:
                    pass
    res['aprime'] = FZ_FMT % aprime(TP, TN, FP, FN)
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
    results['otXimrt'] = F_FMT % np.mean(incorr_rt)
    #  Incorrect mean RT SD
    results['otXisdrt'] = FZ_FMT % np.std(incorr_rt)

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


def LDRC1_NBACK(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)

    results = {}

    try:
        m1_trials = [x for x in dl if x['runList'] == 'M1' and x['M1'] != '.']
        m2_trials = [x for x in dl if x['runList'] == 'M2' and x['M2'] != '.']
        m3_trials = [x for x in dl if x['runList'] == 'M3' and x['M3'] != '.']
        m4_trials = [x for x in dl if x['runList'] == 'M4' and x['M4'] != '.']
    except KeyError:
        raise errors.BadDataError("Key error")
    except ValueError:
        raise errors.BadDataError("Bad value in List3.Sample column")

    m_trials = (m1_trials, m2_trials, m3_trials, m4_trials)
    m_text = ('m1', 'm2', 'm3', 'm4')
    total_trials = 0
    total_correct = 0
    for m_data, m in zip(m_trials, m_text):
        # loop through trained, untrained, high, low and
        # correct responses are equal to 1
        mission_trials = 0
        mission_correct = 0
        for trial_type in ('high', 'low', 'untrained', 'trained'):
            trials = [x for x in m_data if x['type'] == trial_type]
            mission_trials += len(trials)
            total_trials += len(trials)
            corr = [x for x in trials if x['stim.RESP'] == '1']
            mission_correct += len(corr)
            total_correct += len(corr)
            try:
                acc = float(len(corr)) / len(trials) * 100
            except ZeroDivisionError:
                raise errors.BadDataError('Divide by zero in %s' % trial_type)
            results['%s_%s_acc' % (m, trial_type)] = F_FMT % acc

        # Do repeats
        repeat_trials = [x for x in m_data if x['type'] == 'repeat']
        total_trials += len(repeat_trials)
        repeat_corr = 0
        for tr in repeat_trials:
            current_ind = int(tr['List3.Sample'])
            try:
                next_repeat = [x for x in repeat_trials
                               if int(x['List3.Sample']) == (current_ind+1)][0]
                if tr['stim.RESP'] == '1':
                    repeat_corr += 1
            except IndexError:
                #  Correct response here is 2
                if tr['stim.RESP'] == '2':
                    repeat_corr += 1
        total_correct += repeat_corr
        try:
            repeat_acc = float(repeat_corr) / len(repeat_trials) * 100
        except ZeroDivisionError:
            raise errors.BadDataError('Divide by zero in repeat')
        results['%s_repeat_acc' % m] = F_FMT % repeat_acc

        #  Do mission level total accuracy
        mission_correct += repeat_corr
        mission_trials += len(repeat_trials)
        try:
            mission_acc = float(mission_correct) / mission_trials * 100
        except ZeroDivisionError:
            raise errors.BadDataError('Divide by zero in total')
        results['%s_acc' % m] = F_FMT % mission_acc
    total_acc = float(total_correct) / total_trials * 100
    results['all_acc'] = F_FMT % total_acc
    return results


def LDRC1_SENT(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)

    results = {}

    try:
        m1_trials = [x for x in dl if int(x['Blocks.Sample']) < 26]
        m2_trials = [x for x in dl if 25 < int(x['Blocks.Sample']) < 51]
        m3_trials = [x for x in dl if 50 < int(x['Blocks.Sample']) < 76]
        m4_trials = [x for x in dl if 75 < int(x['Blocks.Sample']) < 101]
        m5_trials = [x for x in dl if 100 < int(x['Blocks.Sample']) < 126]
        m6_trials = [x for x in dl if 125 < int(x['Blocks.Sample'])]
    except (KeyError, ValueError):
        raise errors.BadDataError("Couldn't seperate missions")

    m_loop = zip((m1_trials, m2_trials, m3_trials, m4_trials, m5_trials, m6_trials),
                 ('m1', 'm2', 'm3', 'm4', 'm5', 'm6'))

    total = {}
    for m_data, m in m_loop:
        response_trials = [x for x in m_data if x['decideScreen'] == '1']
        m_results = {'tot': 0, 'rt': [], 'corr': 0, 'omit': 0, 'comit': 0}
        #  Loop in the response trials for types
        for rtype in ('semantic', 'truesent', 'pseudo', 'syntatic', 'realword'):
            #  Redcap needs lowered keys
            if not rtype in total:
                #  Init the rtype in total
                total[rtype] = {'tot': 0, 'rt': [], 'corr': 0, 'omit': 0, 'comit': 0}

            responses = [x for x in response_trials if x['type'].lower() == rtype]
            #  Omit is no response
            omit = [x for x in responses if x['DecideScreen.RESP'] == '']
            r_omit = len(omit)
            responses[:] = filter(lambda x: x['DecideScreen.RESP'] != '', responses)
            if len(responses) > 0:
                r_tot = len(responses)

                corr = [x for x in responses if x['correct'] == x['DecideScreen.RESP']]
                r_corr = len(corr)
                r_acc = float(r_corr) / r_tot * 100

                if r_corr > 0:
                    #  RT for correct
                    r_rt = [float(x['DecideScreen.RT']) for x in corr]
                    r_rtavg = np.mean(np.array(r_rt))
                    #  Can't do sd on a one array vector...
                    if len(corr) > 1:
                        r_rtsd = np.std(np.array(r_rt), ddof=1)
                    else:
                        r_rtsd = 0
                else:
                    r_rt = []
                    r_rtavg = -1
                    r_rtsd = 0

                #  Now do incorr
                incorr = [x for x in responses if x['correct'] != x['DecideScreen.RESP']]

                #  Comit is wrong response
                comit = [x for x in incorr if x['DecideScreen.RESP'] != '']
                r_comit = len(comit)
            else:
                r_tot = 0
                r_corr = 0
                r_acc = 0.000
                r_rt = []
                r_rtavg = 0
                r_rtsd = 0
                r_omit = 0
                r_comit = 0

            #  Now fill in everything
            #  Total responses
            results['%s_%s_tot' % (m, rtype)] = D_FMT % r_tot
            m_results['tot'] += r_tot
            total[rtype]['tot'] += r_tot

            #  Accuracy
            results['%s_%s_acc' % (m, rtype)] = F_FMT % r_acc

            #  correct responses
            #  Not going in mission/type
            m_results['corr'] += r_corr
            total[rtype]['corr'] += r_corr

            #  Add to Reaction time lists
            m_results['rt'].extend(r_rt)
            total[rtype]['rt'].extend(r_rt)

            #  RT Mean and SD
            results['%s_%s_corr_rtavg' % (m, rtype)] = F_FMT % r_rtavg
            results['%s_%s_corr_rtsd' % (m, rtype)] = FZ_FMT % r_rtsd

            #  Omit
            results['%s_%s_omit' % (m, rtype)] = D_FMT % r_omit
            m_results['omit'] += r_omit
            total[rtype]['omit'] += r_omit

            #  Comit
            results['%s_%s_comit' % (m, rtype)] = D_FMT % r_comit
            m_results['comit'] += r_comit
            total[rtype]['comit'] += r_comit

        #  Do per mission results
        if m_results['tot'] > 0:
            m_tot = m_results['tot']
            m_acc = float(m_results['corr']) / m_results['tot'] * 100
            m_rtavg = np.mean(np.array(m_results['rt']))
            if len(m_results['rt']) > 1:
                m_rtsd = np.std(np.array(m_results['rt']), ddof=1)
            else:
                m_rtsd = 0
            m_omit = m_results['omit']
            m_comit = m_results['comit']
        else:
            m_tot = 0
            m_acc = 0
            m_rtavg = 0.000
            m_rtsd = 0
            m_omit = 0
            m_comit = 0

        results['%s_all_tot' % m] = D_FMT % m_tot
        results['%s_all_acc' % m] = F_FMT % m_acc
        results['%s_all_corr_rtavg' % m] = F_FMT % m_rtavg
        results['%s_all_corr_rtsd' % m] = FZ_FMT % m_rtsd
        results['%s_all_omit' % m] = D_FMT % m_omit
        results['%s_all_comit' % m] = D_FMT % m_comit

    all_results = {'tot': 0, 'corr': 0, 'rt': [], 'comit': 0, 'omit': 0}
    #  Do per type results

    for rtype, rdata in total.items():
        try:
            #  All response type
            results['all_%s_tot' % rtype] = D_FMT % rdata['tot']
            results['all_%s_acc' % rtype] = F_FMT % (float(rdata['corr']) / rdata['tot'] * 100)
            results['all_%s_corr_rtavg' % rtype] = F_FMT % np.mean(np.array(rdata['rt']))
            results['all_%s_corr_rtsd' % rtype] = FZ_FMT % np.std(np.array(rdata['rt']), ddof=1)
            results['all_%s_omit' % rtype] = D_FMT % rdata['omit']
            results['all_%s_comit' % rtype] = D_FMT % rdata['comit']

            #  Combine for all missions/all types
            all_results['tot'] += rdata['tot']
            all_results['corr'] += rdata['corr']
            all_results['rt'].extend(rdata['rt'])
            all_results['comit'] += rdata['comit']
            all_results['omit'] += rdata['omit']
        except ZeroDivisionError:
            raise errors.BadDataError('No response rows for %s' % rtype)

    #  Do all missions/all types
    results['all_all_tot'] = D_FMT % all_results['tot']
    results['all_all_acc'] = F_FMT % (float(all_results['corr']) / all_results['tot'] * 100)
    results['all_all_corr_rtavg'] = F_FMT % np.mean(np.array(all_results['rt']))
    results['all_all_corr_rtsd'] = FZ_FMT % np.std(np.array(all_results['rt']), ddof=1)
    results['all_all_comit'] = D_FMT % all_results['comit']
    results['all_all_omit'] = D_FMT % all_results['omit']

    return results


def ARN_REP(fobj, new_fname):
    dl = io.split_dict(fobj, new_fname)

    results = {}
    try:
        m1_trials = [x for x in dl if x['runList'] == 'M1']
        m2_trials = [x for x in dl if x['runList'] == 'M2']
        m3_trials = [x for x in dl if x['runList'] == 'M3']
        m4_trials = [x for x in dl if x['runList'] == 'M4']
    except (KeyError, ValueError):
        raise errors.BadDataError('Couldn\'t separate missions')

    m_loop = zip((m1_trials, m2_trials, m3_trials, m4_trials),
                 ('m1', 'm2', 'm3', 'm4'))
    total_correct = []
    total_len = len(dl)
    total_omit = 0
    total_comit = 0
    for m_data, m in m_loop:
        loop_data = zip(('word', 'pseudoword'),
                        ('6', '5'),
                        ('5', '6'))
        mission_correct = []
        mission_total = len(m_data)
        mission_omit = 0
        mission_comit = 0
        for stype, corr_resp, incorr_resp in loop_data:
            trials = filter(lambda x: x['type'] == stype, m_data)
            #  N omit
            omit = filter(lambda x: x['stim.RESP'] not in (corr_resp, incorr_resp), trials)
            mission_omit += len(omit)
            # Remove omits fro mtrials
            trials[:] = filter(lambda x: x['stim.RESP'] in (corr_resp, incorr_resp), trials)
            correct = filter(lambda x: x['stim.RESP'] == corr_resp, trials)
            mission_correct.extend(correct)

            # Accuracy = # of correct / # of trials * 100
            acc = (float(len(correct)) / len(trials)) * 100
            results['%s_%s_acc' % (m, stype)] = F_FMT % acc

            correct_rt = np.array([float(t['stim.RT']) for t in correct])
            rtavg = np.mean(correct_rt)
            results['%s_%s_mrt' % (m, stype)] = F_FMT % rtavg

            rtsd = np.std(correct_rt, ddof=1)
            results['%s_%s_rtsd' % (m, stype)] = FZ_FMT % rtsd

            # N comit
            comit = filter(lambda x: x['stim.RESP'] == incorr_resp, trials)
            mission_comit += len(comit)
            results['%s_%s_omit' % (m, stype)] = D_FMT % len(omit)
            results['%s_%s_comit' % (m, stype)] = D_FMT % len(comit)
        #  Do mission level stuff
        m_acc = (float(len(mission_correct)) / mission_total) * 100
        results['%s_acc' % m] = F_FMT % m_acc

        m_rt = np.array([float(t['stim.RT']) for t in mission_correct])
        m_mrt = np.mean(m_rt)
        results['%s_mrt' % m] = F_FMT % m_mrt
        m_rtsd = np.std(m_rt, ddof=1)
        results['%s_rtsd' % m] = FZ_FMT % m_rtsd

        results['%s_omit' % m] = D_FMT % mission_omit
        total_omit += mission_omit
        results['%s_comit' % m] = D_FMT % mission_comit
        total_comit += mission_comit

        total_correct.extend(mission_correct)

    # Do all mission stuff
    all_acc = (float(len(total_correct)) / total_len) * 100
    results['all_acc'] = F_FMT % all_acc

    all_rt = np.array([float(t['stim.RT']) for t in total_correct])
    all_mrt = np.mean(all_rt)
    all_rtsd = np.std(all_rt, ddof=1)
    results['all_mrt'] = F_FMT % all_mrt
    results['all_rtsd'] = F_FMT % all_rtsd

    results['all_omit'] = D_FMT % total_omit
    results['all_comit'] = D_FMT % total_comit
    return results


def declearn_get_rt(trial):
    responses = ('1', '5')
    if trial['Stimulus.RESP'] in responses:
        return int(trial['Stimulus.RT'])
    elif trial['WaitForResponse.RESP'] in responses:
        return int(trial['WaitForResponse.RTTime']) - int(trial['Stimulus.OnsetTime'])
    else:
        return 0


def declearn_is_correct(trial, corr):
    sk = 'Stimulus.RESP'
    wk = 'WaitForResponse.RESP'
    if trial[sk] in ('1', '5'):
        return trial[sk] == corr
    else:
        return trial[wk] == corr


DECLEARN_NONREAL_SUBSTRINGS = ['potter', 'Plank', 'Laine', 'kirk', 'Eals']


def declearn_is_nonreal(trial):
    return any(map(lambda x: x in trial['Item'], DECLEARN_NONREAL_SUBSTRINGS))


def declearn_is_real(trial):
    return all(map(lambda x: x not in trial['Item'], DECLEARN_NONREAL_SUBSTRINGS))


def declearn_dprime(real_trials, nonreal_trials):
    # dprime
    hit = float(len(filter(lambda x: declearn_is_correct(x, '1'), real_trials)))
    miss = float(len(filter(lambda x: not declearn_is_correct(x, '1'), real_trials)))
    fa = float(len(filter(lambda x: not declearn_is_correct(x, '5'), nonreal_trials)))
    cr = float(len(filter(lambda x: declearn_is_correct(x, '5'), nonreal_trials)))

    HR = hit / (hit + miss)
    FAR = fa / (fa + cr)
    from scipy.stats import norm
    zhr = norm.ppf(HR)
    zfar = norm.ppf(FAR)

    dprime = zhr - zfar
    return dprime


def LERDP2B_DLPICENC(fobj, new_fname=None):
    dl = io.split_dict(fobj, new_fname)

    exp_trials = filter(lambda x: x['Running[Trial]'] == 'EncodingItems', dl)

    nonreal_trials = filter(declearn_is_nonreal, exp_trials)
    assert len(nonreal_trials) == 32
    real_trials = filter(declearn_is_real, exp_trials)
    assert len(real_trials) == 32

    loop = zip([real_trials, nonreal_trials], ['1', '5'], ['real', 'nonreal'])
    data = {}
    for trials, correct_response, key in loop:
        correct_trials = filter(lambda x: declearn_is_correct(x, correct_response), trials)
        incorrect_trials = filter(lambda x: not declearn_is_correct(x, correct_response), trials)
        data['dlpicenc_%s_acc' % key] = '%0.3f' % (float(len(correct_trials)) / len(trials) * 100)
        correct_rts = np.array(filter(None, map(declearn_get_rt, correct_trials)))
        incorrect_rts = np.array(filter(None, map(declearn_get_rt, incorrect_trials)))

        # correct
        data['dlpicenc_%s_corr_rtavg' % key] = '%0.3f' % np.mean(correct_rts)
        data['dlpicenc_%s_corr_rtsd' % key] = '%0.3f' % np.std(correct_rts, ddof=1)
        # incorrect
        data['dlpicenc_%s_incorr_rtavg' % key] = '%0.3f' % np.mean(incorrect_rts)
        data['dlpicenc_%s_incorr_rtsd' % key] = '%0.3f' % np.std(incorrect_rts, ddof=1)

    data['dlpicenc_dprime'] = '%0.3f' % declearn_dprime(real_trials, nonreal_trials)
    return data


def is_old(trial):
    seen_objects = set(['legos', 'tape', 'hippopotamus', 'Plank13', 'Plank4', 'watering-can',
                        'Plank17', 'matches', 'Laine-RIITMOTT', 'camcorder', 'saturn', 'Plank3',
                        'kirk1', 'barbell', 'Laine-JYRSIN', 'chimney', 'Plank50', 'hamster',
                        'Eals10', 'vacuum', 'Plank49', 'platypus', 'ruler', 'strainer', 'Laine-kosseli',
                        'tepee', 'Eals22', 'potter26', 'Eals23', 'teapot', 'Laine-ROVE', 'potter9',
                        'crab', 'hose', 'potter17', 'battleship', 'dolphin', 'floss', 'potter7',
                        'headphones', 'Laine-PALIN', 'stoplight', 'Plank5', 'Laine-naskain', 'potter22',
                        'sloth', 'potter12', 'yo-yo', 'Laine-KALKKU', 'ladybug', 'lighthouse', 'potter8',
                        'Laine-karttu', 'Laine-pynna', 'plant', 'trombone', 'Eals08', 'potter15', 'Laine-NORHA',
                        'llama', 'shark', 'Laine-MAALITSA', 'Eals29', 'needle'])
    return trial['Item'] in seen_objects


def recog_is_correct(trial):
    corr_response = '1' if is_old(trial) else '5'
    return declearn_is_correct(trial, corr_response)


def LERDP2B_DLPICREC(fobj, new_fname=None):
    dl = io.split_dict(fobj, new_fname)

    exp_trials = filter(lambda x: x['Running[Trial]'] == 'RetrievalItems', dl)
    old_trials = filter(is_old, exp_trials)
    assert len(old_trials) == 64
    novel_trials = filter(lambda x: not is_old(x), exp_trials)
    assert len(novel_trials) == 64

    loop = zip([old_trials, novel_trials], ['1', '5'], ['old', 'novel'])
    data = {}
    for trials, correct_response, key in loop:
        correct_trials = filter(recog_is_correct, trials)
        incorrect_trials = filter(lambda x: not recog_is_correct(x), trials)
        data['dlpicrec_%s_acc' % key] = '%0.3f' % (float(len(correct_trials)) / len(trials) * 100)
        correct_rts = np.array(filter(None, map(declearn_get_rt, correct_trials)))
        incorrect_rts = np.array(filter(None, map(declearn_get_rt, incorrect_trials)))

        # correct
        data['dlpicrec_%s_corr_rtavg' % key] = '%0.3f' % np.mean(correct_rts)
        data['dlpicrec_%s_corr_rtsd' % key] = '%0.3f' % np.std(correct_rts, ddof=1)
        # incorrect
        data['dlpicrec_%s_incorr_rtavg' % key] = '%0.3f' % np.mean(incorrect_rts)
        data['dlpicrec_%s_incorr_rtsd' % key] = '%0.3f' % np.std(incorrect_rts, ddof=1)
    data['dlpicrec_dprime'] = '%0.3f' % declearn_dprime(old_trials, novel_trials)
    return data


def RCV_PASSAGES(fobj, new_fname=None):
    dl = io.split_dict(fobj, new_fname)

    try:
        m1_trials = filter(lambda x: x['Block'] == '1', dl)
        m2_trials = filter(lambda x: x['Block'] == '2', dl)
        m3_trials = filter(lambda x: x['Block'] == '3', dl)
        m4_trials = filter(lambda x: x['Block'] == '4', dl)
    except KeyError:
        raise errors.BadDataError("Couldn't split missions")

    def rep_pct(trials):
        resp = ('5', '6')
        rep_trials = filter(lambda x: x['Repeat'] == '1', trials)
        corr_reps = filter(lambda x: x['Stim.RESP'] in resp or x['Ch.RESP'] in resp, rep_trials)
        return (float(len(corr_reps)) / len(rep_trials)) * 100

    def pic_pct(trials):
        try:
            dt = filter(lambda x: x['decideScreen'] == '1', trials)[0]
            num_correct = float(sum(map(int, [dt['Picts2.ACC'], dt['Picts1.ACC']])))
            return (num_correct / 2) * 100
        except KeyError:
            return ''

    data = {}
    loop = zip((m1_trials, m2_trials, m3_trials, m4_trials),
               ('m1', 'm2', 'm3', 'm4'))
    for trials, mis in loop:
        pic_result = pic_pct(trials)
        rep_result = rep_pct(trials)
        data['%s_pic_pct' % mis] = FZ_FMT % pic_result if pic_result else ''
        data['%s_rep_pct' % mis] = FZ_FMT % rep_result if rep_result else ''
    return data


def LERD_SRT(fobj, new_fname=None):
    dl = io.split_dict(fobj, new_fname)

    try:
        m1 = filter(lambda x: x['Block'] == '1', dl)
        m2 = filter(lambda x: x['Block'] == '2', dl)
        assert len(m1) == len(m2) and len(m1) == 312
    except (KeyError, AssertionError):
        raise errors.BadDataError('Could not split missions')

    d = {}

    def compute_block(block):
        F = '%0.3f'
        acc, acc_rtavg, acc_rtstd = 0, 0, 0
        try:
            ntrials = len(block)
            acc_trials = filter(lambda x: x['Target.ACC'] == '1', block)

            acc = len(acc_trials) / float(ntrials) * 100
            acc_rt = np.array(map(lambda x: float(x['Target.RT']), acc_trials))
            acc_rtavg = acc_rt.mean()
            acc_rtstd = acc_rt.std()
        except:
            pass

        return F % acc, F % acc_rtavg, F % acc_rtstd

    loop = zip([m1, m2], ['m1', 'm2'])
    for block, mname in loop:
        acc, rt_avg, rt_std = compute_block(block)
        d['%s_all_acc' % mname] = acc
        d['%s_all_rtavg' % mname] = rt_avg
        d['%s_all_rtstd' % mname] = rt_std

        imp = filter(lambda x: x['Cond'] == '2', block)
        acc, rt_avg, rt_std = compute_block(imp)
        d['%s_imp_acc' % mname] = acc
        d['%s_imp_rtavg' % mname] = rt_avg
        d['%s_imp_rtstd' % mname] = rt_std

        rand = filter(lambda x: x['Cond'] == '1', block)
        acc, rt_avg, rt_std = compute_block(rand)
        d['%s_rand_acc' % mname] = acc
        d['%s_rand_rtavg' % mname] = rt_avg
        d['%s_rand_rtstd' % mname] = rt_std

        # random loop
        rloop = zip([1, 97, 193, 289], [24, 120, 216, 312], ['b1', 'b2', 'b3', 'b4'])
        for mini, maxi, bname in rloop:
            rblock = filter(lambda x: mini <= int(x['BlockList']) <= maxi, rand)
            acc, rt_avg, rt_std = compute_block(rblock)
            d['%s_rand_%s_acc' % (mname, bname)] = acc
            d['%s_rand_%s_rtavg' % (mname, bname)] = rt_avg
            d['%s_rand_%s_rtstd' % (mname, bname)] = rt_std

        # implicit loop
        iloop = zip([25, 49, 73, 121, 145, 169, 217, 241, 265],
                    [48, 72, 96, 144, 168, 192, 240, 264, 288],
                    ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9'])
        for mini, maxi, bname in iloop:
            rblock = filter(lambda x: mini <= int(x['BlockList']) <= maxi, imp)
            acc, rt_avg, rt_std = compute_block(rblock)
            d['%s_imp_%s_acc' % (mname, bname)] = acc
            d['%s_imp_%s_rtavg' % (mname, bname)] = rt_avg
            d['%s_imp_%s_rtstd' % (mname, bname)] = rt_std

    return d


def aprime(tp, tn, fp, fn):
    """
    ---------------
    |      |      |
    |  TP  |  FP  |
    |      |      |
    ---------------
    |      |      |
    |  FN  |  TN  |
    |      |      |
    ---------------
    """
    aprime = 0.0
    try:
        hr = tp / float(tp + fn)
        fa = fp / float(fp + tn)
        aprime = .5 + ((hr - fa) * (1.0 + hr - fa)) / (4.0 * hr * (1.0 - fa))
    except ZeroDivisionError:
        pass
    return aprime
