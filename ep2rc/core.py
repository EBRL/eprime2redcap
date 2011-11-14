#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os

from pdb import set_trace
#  import other grants here
import NF
import NFB
import projects

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
PROJECT_CLASS = {'NF': projects.NF, 'NFB': projects.NFB}

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

def class_from_projstr(proj_str):
    return PROJECT_CLASS[proj_str]

def parse_file(fname, fobj):
    bname = os.path.basename(fname)
    name, ext = os.path.splitext(bname)
    #  PROJECT_BLAHBLAHBLAH
    project = name.split('_')[0]
    proj_class = class_from_projstr(project)
    parser_object = proj_class(fname, fobj)

    #  Parse the file and write out a copy
    to_redcap = parser_object.parse()

    return to_redcap

