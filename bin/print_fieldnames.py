#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This serves to document all the fieldnames for each task 
mi1: Mental imagery from NFRO1
swr1: Single Word Reading from NFRO1
rep1: repitition task from NFRO1
pic1: Picture task from NFRO1
"""




data = {'mi1': {'per_mission': [('imag_rtavg', 'Imaginary Mean RT'),
                                ('imag_rtsd', 'Imaginary RT SD'),
                                ('imag_acc', 'Imaginary Accuracy'),
                                ('imag_accsd', 'Imaginary Accuracy SD'),
                                ('imag_omit', 'Imaginary Omit'),
                                ('imag_fn', 'Imaginary False Negative'),
                                ('imag_fp', 'Imaginary False Positive'),
                                ('cont_rtavg', 'Control Mean RT'),
                                ('cont_rtsd', 'Control RT SD'),
                                ('cont_acc', 'Control Accuracy'),
                                ('cont_accsd', 'Control Accuracy SD'),
                                ('cont_omit', 'Control Omit'),
                                ('cont_fn', 'Control False Negative'),
                                ('cont_fp', 'Control False Positive')],
               'visit': [('pre', 'Pre'),
                         ('post', 'Post')],
               'mission': [('m1', 'Mission1'),
                           ('m2', 'Mission2')],
               'per_visit': [('upload', 'Upload Complete')],
               'form': 'MentalImagery1'},
        'swr1': {'per_mission': [('hai_acc', 'High Abstract Irregular Accuracy'),
                                 ('hai_accsd', 'High Abstract Irregular Accuracy SD'),
                                 ('hai_rtavg', 'High Abstract Irregular Mean RT'),
                                 ('hai_rtsd', 'High Abstract Irregular RT SD'),
                                 ('hai_omit', 'High Abstract Irregular Omit'),
                                 ('hai_comit', 'High Abstract Irregular Comit'),
                                 ('har_acc', 'High Abstract Regular Accuracy'),
                                 ('har_accsd', 'High Abstract Regular Accuracy SD'),
                                 ('har_rtavg', 'High Abstract Regular Mean RT'),
                                 ('har_rtsd', 'High Abstract Regular RT SD'),
                                 ('har_omit', 'High Abstract Regular Omit'),
                                 ('har_comit', 'High Abstract Regular Comit'),
                                 ('hci_acc', 'High Concrete Irregular Accuracy'),
                                 ('hci_accsd', 'High Concrete Irregular Accuracy SD'),
                                 ('hci_rtavg', 'High Concrete Irregular Mean RT'),
                                 ('hci_rtsd', 'High Concrete Irregular RT SD'),
                                 ('hci_omit', 'High Concrete Irregular Omit'),
                                 ('hci_comit', 'High Concrete Irregular Comit'),
                                 ('hcr_acc', 'High Concrete Regular Accuracy'),
                                 ('hcr_accsd', 'High Concrete Regular Accuracy SD'),
                                 ('hcr_rtavg', 'High Concrete Regular Mean RT'),
                                 ('hcr_rtsd', 'High Concrete Regular RT SD'),
                                 ('hcr_omit', 'High Concrete Regular Omit'),
                                 ('hcr_comit', 'High Concrete Regular Comit'),
                                 ('word_acc', 'All Words Accuracy'),
                                 ('word_accsd', 'All Words Accuracy SD'),
                                 ('word_rtavg', 'All Words Mean RT'),
                                 ('word_rtsd', 'All Words RT SD'),
                                 ('word_omit', 'All Words Omit'),
                                 ('word_comit', 'All Words Comit'),
                                 ('nonword_acc', 'Nonword Accuracy'),
                                 ('nonword_accsd', 'Nonword Accuracy SD'),
                                 ('nonword_rtavg', 'Nonword Mean RT'),
                                 ('nonword_rtsd', 'Nonword RT SD'),
                                 ('nonword_omit', 'Nonword Omit'),
                                 ('nonword_comit', 'Nonword Comit')],
                 'visit': [('pre', 'Pre'),
                           ('post', 'Post')],
                 'mission': [('m1', 'Mission1'),
                             ('m2', 'Mission2')],
                 'per_visit': [('upload', 'Upload Complete')],
                 'form': 'SingleWordReading1'},
        'pic1': {'per_mission': [('con_acc', 'Consonant Accuracy'),
                                 ('con_accsd', 'Consonant Accuracy SD'),
                                 ('con_rtavg', 'Consonant Mean RT'),
                                 ('con_rtsd', 'Consonant RT SD'),
                                 ('con_omit', 'Consonant Omit'),
                                 ('con_comit', 'Consonant Comit'),
                                 ('match_acc', 'Match Accuracy'),
                                 ('match_accsd', 'Match Accuracy SD'),
                                 ('match_rtavg', 'Match Mean RT'),
                                 ('match_rtsd', 'Match RT SD'),
                                 ('match_omit', 'Match Omit'),
                                 ('match_comit', 'Match Comit'),
                                 ('psw_acc', 'Pseudowords Accuracy'),
                                 ('psw_accsd', 'Pseudowords Accuracy SD'),
                                 ('psw_rtavg', 'Pseudowords Mean RT'),
                                 ('psw_rtsd', 'Pseudowords RT SD'),
                                 ('psw_omit', 'Pseudowords Omit'),
                                 ('psw_comit', 'Pseudowords Comit'),
                                 ('wrd_acc', 'Words Accuracy'),
                                 ('wrd_accsd', 'Words Accuracy SD'),
                                 ('wrd_rtavg', 'Words Mean RT'),
                                 ('wrd_rtsd', 'Words RT SD'),
                                 ('wrd_omit', 'Words Omit'),
                                 ('wrd_comit', 'Words Comit')],
                'visit': [('pre', 'Pre'),
                          ('post', 'Post')],
                'mission': [('m1', 'Mission1'),
                            ('m2', 'Mission2')],
                'per_visit': [('upload', 'Upload Complete')],
                'form': 'PictureTask1'},
        'rep1': {'per_mission': [('abs_acc', 'Abstract Accuracy'),
                                 ('abs_accsd', 'Abstract Accuracy SD'),
                                 ('abs_rtavg', 'Abstract Mean RT'),
                                 ('abs_rtsd', 'Abstract RT SD'),
                                 ('abs_omit', 'Abstract Omit'),
                                 ('abs_comit', 'Abstract Comit'),
                                 ('conc_acc', 'Concrete Accuracy'),
                                 ('conc_accsd', 'Concrete Accuracy SD'),
                                 ('conc_rtavg', 'Concrete Mean RT'),
                                 ('conc_rtsd', 'Concrete RT SD'),
                                 ('conc_omit', 'Concrete Omit'),
                                 ('conc_comit', 'Concrete Comit'),
                                 ('cons_acc', 'Consonant Accuracy'),
                                 ('cons_accsd', 'Consonant Accuracy SD'),
                                 ('cons_rtavg', 'Consonant Mean RT'),
                                 ('cons_rtsd', 'Consonant RT SD'),
                                 ('cons_omit', 'Consonant Omit'),
                                 ('cons_comit', 'Consonant Comit'),
                                 ('non_acc', 'Nonword Accuracy'),
                                 ('non_accsd', 'Nonword Accuracy SD'),
                                 ('non_rtavg', 'Nonword Mean RT'),
                                 ('non_rtsd', 'Nonword RT SD'),
                                 ('non_omit', 'Nonword Omit'),
                                 ('non_comit', 'Nonword Comit')],
                'visit': [('', '')],
                'mission': [('m1', 'Mission1'),
                            ('m2', 'Mission2'),
                            ('m3', 'Mission3')],
                'per_visit': [('upload', 'Upload Complete')],
                'form': 'RepetitionTask1'},
        'nback1': {'per_mission': [('acc', 'Single Mission Accuracy'),
                                   ('high_acc', 'High Frequency Accuracy'),
                                   ('low_acc', 'Low Frequency Accuracy'),
                                   ('trained_acc', 'Trained Accuracy'),
                                   ('untrained_acc', 'Untrained Accuracy'),
                                   ('repeat_acc', 'Repeat Accuracy')],
                    'visit':[('', '')],
                    'mission': [('m1', 'Mission1'),
                                ('m2', 'Mission2'),
                                ('m3', 'Mission3'),
                                ('m4', 'Mission4')],
                    'per_visit': [('upload', 'Upload Complete'),
                                  ('all_acc', 'All Accuracy')],
                    'form': 'NBack1'}}
                
for task, d in data.items():
    for visit, visit_text in d['visit']:
        for m, m_text in d['mission']:
            for res, res_text in d['per_mission']:
                task_print = [task]
                if visit:
                    task_print.append(visit)
                if m:
                    task_print.append(m)
                task_print.append(res)
                
                print('\t'.join(['_'.join(task_print), d['form'], '', 'text', ' '.join([d['form'], visit_text, m_text, res_text])]))
                # print '_'.join(task_print)
        for res,res_text in d['per_visit']:
            if res:
                task_print = [task]
                if visit:
                    task_print.append(visit)
                task_print.append(res)
                print('\t'.join(['_'.join(task_print), d['form'], '', 'text', ' '.join([d['form'], visit_text, res_text])]))
                # print '_'.join(task_print)
