#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os

from pdb import set_trace
#  import other grants here
import NF
import NFB


#  This maps grants/tasks to the correct parser
TASK_PARSER = {'NF': {'MI': NF.MI,
                      'SWR': NF.SWR,
                      'PIC': NF.PIC,
                      'REP': NF.REP},
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

RC_UNKEY = {'in-magnet': 'id',
            'NF': 'studyid'}
#  Fully implemented grants: THESE MUST BE IN THE ABOVE TWO DICTS
GRANTS = ('NF', 'NFB')


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
    if grant == 'NFB':
        ind_keys = [(1, 'task'), (2, 'behavid'), (3, 'scanid')]
        if parts[1] in ('FIG', 'MI', 'MR', 'OLSON'):
            ind_keys.append((4, 'visit'))
    # elif grant == "RCV":
    for ind, key in ind_keys:
        info[key] = parts[ind]
    return info    

def rc_prefix(info):
    pre = ''
    if info['grant'] == 'NF':
        t = info['task']
        rc_task = GRANT_TASKS['NF'][t]
        if t in ('PIC', 'SWR', 'MI'):
            pre = '%s_%s' % (rc_task, info['visit'].lower())
        else:
            #  No visit for REP task
            pre = '%s' % rc_task
    if info['grant'] == 'NFB':
        #  Don't worry about checking NFB
        pass
    #  Add other grants here
    return pre

def upload_key(info):
    key = ''
    if info['database'] == 'in-magnet':
        key = '%s_upload' % rc_prefix(info)
    return key
    
def nfb_visit(info):
    if info['visit'] == 'Pre':
        to_ret = '1'
    elif info['visit'] == 'Post':
        to_ret =  '2'
    else:
        to_ret = 'X'
    return to_ret

def key_map(info):
    if info['grant'] == 'NF':
        f = lambda x,y: '%s_%s' % (rc_prefix(x), y)
    if info['grant'] == 'NFB':
        f = lambda x,y: y.replace('X', nfb_visit(x))
        if info['task'] == 'SENT':
            f = lambda x,y: y
    return f

def is_outmagnet(grant):
    #  If return true, make sure to return the grant it corresponds to
    if grant == 'NF':
        return (False, 'in-magnet')
    if grant == "NFB":
        return (True, 'NF')

def copy_fname(info, bname):
    _platform = os.uname()[0]
    if _platform == 'Linux':
        prefix = os.path.join('/', 'fs0')
    else:
        prefix = os.path.join(os.path.expanduser('~'), 'Code', 'eprime2redcap')
    out, new_g = is_outmagnet(info['grant'])
    if out:  # Is out of magnet
        grant = new_g
        where = 'Out_Behavioral'
        subj_dir = (info['behavid'],)
    else:
        grant = info['grant']
        where = 'In_Behavioral'
        subj_dir = (info['behavid'], info['scanid'])
    new_dir = os.path.join(prefix, 'New_Server', grant, where, '_'.join(subj_dir))
    # Make dirs if necessary
    if not os.path.isdir(new_dir):
        os.makedirs(new_dir)
    return os.path.join(new_dir, bname+'.txt')


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
        km = key_map(info)
        for k, v in data.items():
            to_redcap[km(info, k)] = v
        out, db = is_outmagnet(info['grant'])
        if out:
            if db == 'NF':
                #  Remove this if
                to_redcap[RC_UNKEY[db]] = info['behavid']
        else:
            #  Fill out grant and id
            to_redcap['grant'] = info['grant']
            to_redcap['id'] = '%s_%s' % (info['behavid'], info['scanid'])
            #  Fill out upload field
            to_redcap[upload_key(info)] = 'yes'
    return to_redcap

