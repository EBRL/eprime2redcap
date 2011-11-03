#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os

#  import other grants here
import NFRO1


#  This maps grants/tasks to the correct parser
TASK_PARSER = {'NF':{'MI': NFRO1.MI,
                     'SWR': NFRO1.SWR,
                     'PIC': NFRO1.PIC,
                      'REP': NFRO1.REP}}
TASK_PARSER = {'NF': {'MI': NFRO1.MI,
                      'SWR': NFRO1.SWR,
                      'PIC': NFRO1.PIC,
                      'REP': NFRO1.REP},
               'NFB': {'MR': NFB.MR,
                       'FIG': NFB.FIG,
                       'MI': NFB.MI,
                       'OLSON': NFB.OLSON,
                       'SENT': NFB.SENT}}
#  This maps grants/tasks to the correct redcap prefix
GRANT_TASKS = {'NF': {'MI': 'mi1',
                      'SWR': 'swr1',
                      'PIC': 'pic1',
                      'REP': 'rep1'}}

#  Fully implemented grants: THESE MUST BE IN THE ABOVE TWO DICTS
GRANTS = ('NF',)


all_tasks = []
for _, tasks in TASK_PARSER.items():
    all_tasks.extend(tasks.keys())
TASKS = set(all_tasks)

def parse_fname(grant, fname):
    info = {}
    info['grant'] = grant
    
    parts = fname.split('_')
    
    if grant == 'NF':
        #  at least NF_TASK_BEHAVID_SCNAID
        ind_keys = [(1, 'task'), (2, 'behavid'), (3, 'scanid')]
        if parts[1] in ('SWR', 'PIC', 'MI'):
            #  GRANT_TASK_BEHAVID_SCANID_VISIT
            ind_keys.append((4, 'visit'))
        if parts[1] in ('SWR', 'PIC'):
            #  GRANT_TASK_BEHAVID_SCANID_VISIT_LIST
            ind_keys.append((5, 'list'))
    #  Add more grants here
    # elif grant == "RCV":
    for ind, key in ind_keys:
        info[key] = parts[ind]
    return info    

def rc_prefix(info):
    if info['grant'] == 'NF':
        t = info['task']
        rc_task = GRANT_TASKS['NF'][t]
        if t in ('PIC', 'SWR', 'MI'):
            pre = '%s_%s' % (rc_task, info['visit'].lower())
        else:
            #  No visit for REP task
            pre = '%s' % rc_task
    #  Add other grants here
    return pre

def upload_key(info):
    return '%s_upload' % rc_prefix(info)

def copy_fname(info, bname):
    _platform = os.uname()[0]
    if _platform == 'Linux':
        prefix = os.path.join('/', 'fs0', 'New_Server')
    else:
        prefix = os.path.join(os.path.expanduser('~'), 'Code', 'eprime2redcap')
    new_dir = os.path.join(prefix, grant, behav, '%s_%s' % (info['behavid'], info['scanid']))
    # Make dirs if necessary
    if not os.path.isdir(new_dir):
        os.makedirs(new_dir)
    return os.path.join(new_dir, bname)


def parse_file(fname, fobj):
    bname = os.path.basename(fname)
    name, ext = os.path.splitext(bname)
    #  GRANT_TASK_BEHAVID_SCANID_EXTRA
    parts = name.split('_')
    grant = parts[0]
    info = parse_fname(grant, name)        
    parser = TASK_PARSER[grant][info['task']]

    #  Parse the file and write out a copy
    data = parser(fobj, copy_fname(info, name))
    to_redcap = {}
    if data:
        pre = rc_prefix(info)
        for k, v in data.items():
            to_redcap['%s_%s' % (pre, k)] = v
        #  Fill out grant and id
        to_redcap['grant'] = info['grant']
        to_redcap['id'] = '%s_%s' % (info['behavid'], info['scanid'])
        #  Fill out upload field
        to_redcap[upload_key(info)] = 'yes'
    return to_redcap

