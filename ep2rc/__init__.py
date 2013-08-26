#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'
__version__ = '0.5.2'

from stathat import StatHat
_stats = StatHat('scott.s.burns@gmail.com')
from os import path

from core import parse_file
from rc import upload
from errors import BadDataError


def parse_and_upload(fname, database, do_upload=True):
    msg = ''
    try:
        to_redcap = {}
        with open(fname) as f:
            to_redcap = parse_file(fname, f)
    except BadDataError as e:
        msg = "(%s)" % e + " Failed with %s" % fname
    suc = False
    if to_redcap and do_upload:
        suc = upload(to_redcap, database)
    if suc:
        msg = "Success with %s" % fname
    print msg
    return to_redcap, suc


def switchboard_fxn(**kwargs):
    from redcap import Project, RedcapError
    from secret import TOKENS, URL
    pidform2field = {(8070, 'eprime'): (['sentcomp_file', 'dlpic_enc_file', 'dlpic_rec_file', 'srtb_file'], 'rc', 'RC'),
                     (8070, 'imaging'): (['passages_eprime_file'], 'in-magnet', 'RC'),
                     (14707, 'visit_1_behavioral'): (['v1_dlpic_enc_file', 'v1_dlpic_rec_file'], 'lerdp2', 'LERDP2'),
                     (9257, 'imaging'): (['passages_eprime_file'], 'in-magnet', 'RCLMS'),
                     (9259, 'imaging'): (['lerdlms_srt_eprime', 'lerdlms_pic_eprime'], 'in-magnet', 'NPR'),
                     (13529, 'imaging'): (['srt_file', 'pic2_file'], 'in-magnet', 'LERDP2_IMAGING')}
    fields, db, project_token_key = pidform2field.get((kwargs['pid'], kwargs['form']))
    project = Project(URL, TOKENS[project_token_key])
    record = kwargs['record']
    for field in fields:
        try:
            content, headers = project.export_file(record=record, field=field)
            fullfile = path.join('/home/burnsss1/temp/', headers['name'])
            with open(fullfile, 'w') as f:
                f.write(content)
            print "ep2rc.switchboard_fxn: Running parse_and_upload on %s" % fullfile
            to_redcap, success = parse_and_upload(fullfile, db)
            _stats.count('ep2rc', 1)
            if not success:
                print "ep2rc.switchboard_fxn: Failed uploading results for %s" % record
                _stats.count('ep2rc error', 1)
        except RedcapError:
            pass
