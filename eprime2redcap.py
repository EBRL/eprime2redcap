#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

#  Import when we have API key
#  import rc_upload
import NFRO1

#  This maps grants/tasks to the correct parser
TASK_PARSER = {'NF':{'MI': NFRO1.MI,
                     'SWR': NFRO1.SWR,
                     'PIC': NFRO1.PIC,
                      'REP': NFRO1.REP}}
#  This maps grants/tasks to the correct redcap prefix
GRANT_TASKS = {'NF': {'MI': 'mi1',
                      'SWR': 'swr1',
                      'PIC': 'pic1',
                      'REP': 'rep1'}}

def arguments():
    import argparse
    ap = argparse.ArgumentParser()
    
    #  Arguments
    ap.add_argument('-f', dest='file',
        help='Parse and upload data from a (properly named) file')
    return ap.parse_args()

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

def parse_file(fname, fobj):
    bname = os.path.basename(fname)
    name, ext = os.path.splitext(bname)
    #  GRANT_TASK_BEHAVID_SCANID_EXTRA
    parts = name.split('_')
    grant = parts[0]
    info = parse_fname(grant, name)        
    parser = TASK_PARSER[grant][info['task']]

    #  Parse the file
    data = parser(fobj)
    to_redcap = {}
    pre = rc_prefix(info)
    for k, v in data.items():
        to_redcap['%s_%s' % (pre, k)] = v
    to_redcap['grant'] = info['grant']
    to_redcap['id'] = '%s_%s' % (info['behavid'], info['scanid'])
    return to_redcap

def upload(data):
    success = rc_upload.upload(data)
    if not success:
        from pprint import pprint
        print("Failed to upload to redcap. See below for data for manual entry.")
        pprint(data)

if __name__ == '__main__':
    args = arguments()

    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError("This file doesn't exist")
        with open(args.file) as f:
            to_redcap =  parse_file(args.file, f)
        upload(to_redcap)