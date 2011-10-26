#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This serves to document all the fieldnames for each task 
mi1: Mental imagery from NFRO1
swr1: Single Word Reading from NFRO1
rep1: repitition task from NFRO1
pic1: Picture task from NFRO1
"""




data = {'mi1': {'per_mission': ['imag_rtavg', 'imag_rtsd', 'imag_acc', 'imag_accsd',
                          'imag_omit', 'imag_fn', 'imag_fp',
                          'cont_rtavg', 'cont_rtsd', 'cont_acc', 'cont_accsd',
                          'cont_omit', 'cont_fn', 'cont_fp'],
               'visit': ['pre', 'post'],
               'mission': ['m1', 'm2'],
               'per_visit': ['upload']},
        'swr1': {'per_mission': ['hai_acc', 'hai_accsd', 'hai_rtavg', 'hai_rtsd',
                             'hai_omit', 'hai_comit', 'har_acc', 'har_accsd',
                             'har_rtavg', 'har_rtsd', 'har_omit', 'har_comit',
                             'hci_acc', 'hci_accsd', 'hci_rtavg', 'hci_rtsd',
                             'hci_omit', 'hci_comit','hcr_acc', 'hcr_accsd',
                             'hcr_rtavg', 'hcr_rtsd', 'hcr_omit', 'hcr_comit',
                             'word_acc', 'word_accsd', 'word_rtavg',
                             'word_rtsd','word_omit', 'word_comit',
                             'nonword_acc', 'nonword_accsd', 'nonword_rtavg',
                             'nonword_rtsd', 'nonword_omit', 'nonword_comit'],
                 'visit': ['pre', 'post'],
                 'mission': ['m1', 'm2'],
                 'per_visit': ['upload']},
        'pic1': {'per_mission': ['con_acc', 'con_accsd', 'con_rtavg', 'con_rtsd',
                             'con_omit', 'con_comit', 'match_acc', 'match_accsd',
                             'match_rtavg', 'match_rtsd', 'match_omit', 'match_comit',
                             'psw_acc', 'psw_accsd', 'psw_rtavg', 'psw_rtsd',
                             'psw_omit', 'psw_comit', 'wrd_acc', 'wrd_accsd',
                             'wrd_rtavg', 'wrd_rtsd', 'wrd_omit', 'wrd_comit'],
                'visit': ['pre', 'post'],
                'mission': ['m1', 'm2'],
                'per_visit': ['upload']},
        'rep1': {'per_mission': ['abs_acc', 'abs_accsd', 'abs_rtavg', 'abs_rtsd',
                             'abs_omit', 'abs_comit', 'conc_acc', 'conc_accsd',
                             'conc_rtavg', 'conc_rtsd', 'conc_omit', 'conc_comit',
                             'cons_acc', 'cons_accsd', 'cons_rtavg', 'cons_rtsd',
                             'cons_omit', 'cons_comit', 'non_acc', 'non_accsd',
                             'non_rtavg', 'non_rtsd', 'non_omit', 'non_comit'],
                'visit': [''],
                'mission': ['m1', 'm2', 'm3'],
                'per_visit': ['upload']}}
                
for task, d in data.items():
    for visit in d['visit']:
        for m in d['mission']:
            for res in d['per_mission']:
                to_print = [task]
                if visit:
                    to_print.append(visit)
                if m:
                    to_print.append(m)
                to_print.append(res)
                print '_'.join(to_print)
        for res in d['per_visit']:
            if res:
                to_print = [task]
                if visit:
                    to_print.append(visit)
                to_print.append(res)
                print '_'.join(to_print)
