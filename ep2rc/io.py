#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

""" This module should be used by grant files for reading/writing """

def split_dict(fobj, new_fname=None):
    """ Decode and split a file"""

    raw = fobj.read()
    raw_sp = raw.split('\r\n')
    raw_sp[:] = filter(lambda x: x != '', raw_sp)

    if new_fname:
        with open(new_fname) as f:
            f.write('\n'.join(raw_sp))

    good = []
    good = [r.split('\t') for r in raw_sp]

    dict_list = []
    #  Loop through trials, skipping header
    for trial in good[1:]:
        trial_d = {}
        #  Loop through column headers
        for i, key in enumerate(good[0]):
            try:
                trial_d[key] = trial[i].replace('@', '')
            except IndexError:
                print("Skipping %s for trial #%d" % (key, good.index(trial)))
                pass
        dict_list.append(trial_d)
    return dict_list 
