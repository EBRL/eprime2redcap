#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os

from . import projects

TASKS = ('MI', 'SWR', 'PIC', 'REP', 'MR', 'FIG', 'MI', 'OLSON', 'SENT', 'NBACK', 'PASSAGES',
         'DLPICENC', 'DLPICREC', 'SRT', 'PIC2', 'SYM', 'NONSYM')

PROJECT_CLASS = {'RCK': projects.RCK,
                 'NF': projects.NF,
                 'NFB': projects.NFB,
                 'RCVB': projects.RCVB,
                 'LERDB': projects.LERDB,
                 'LDRC1': projects.LDRC1,
                 'ARN': projects.ARN,
                 'RCV': projects.RCV,
                 'LERDP2': projects.LERDP2,
                 'RCLMS': projects.RCLMS,
                 'LERDP2I': projects.LERDP2I,
                 'LERDLMS': projects.LERDLMS}

#  Fully implemented grants: THESE MUST BE IN THE ABOVE TWO DICTS PROJECT_CLASS
PROJECTS = ('NF', 'NFB', 'RCVB', 'LERDB', 'LDRC1', 'ARN', 'RCK', 'RCV', 'LERDP2', 'RCLMS', 'LERDLMS')


def upload_key(info):
    fields = ('grant', 'task', 'id', 'visit', 'list')
    good_fields = [f for f in fields if f in info]
    fname = '_'.join([info.get(f) for f in good_fields]) + '.txt'
    proj = class_from_projstr(info['grant'])(fname, None, database=info['database'])
    return proj.upload_key()


def class_from_projstr(proj_str):
    return PROJECT_CLASS[proj_str]


def parse_file(fname, fobj, database='in-magnet'):
    bname = os.path.basename(fname)
    name, ext = os.path.splitext(bname)
    #  PROJECT_BLAHBLAHBLAH
    project = name.split('_')[0]
    try:
        proj_class = class_from_projstr(project)
    except KeyError:
        raise ValueError("This project hasn't been implemented")
    parser_object = proj_class(fname, fobj, database)

    #  Parse the file and write out a copy
    return parser_object.parse()
