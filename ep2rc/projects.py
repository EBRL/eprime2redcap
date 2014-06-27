#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os

from . import parsers as pf
""" A new project must have:
self.parsers = {...} in __init__
self.copy_dir = os.path.join(...) in __init__
def parse_fname(self): that at least calls self.split_fname
def key_map(self): that at least returns lambda x: x
def project_additions(self): that returns at least {}

And it should get a unit test
"""


class BaseProject(object):
    """ Base class from which all Projects should inherit"""

    def __init__(self, fname, fobj, database='in-magnet'):
        """ Constructor """
        #  Required info
        self.fname = fname
        self.fobj = fobj
        self.database = database

        self.project = None
        self.task = None
        self.behavid = None
        self.scanid = None

        self.parse_fname()

    def prefix(self):
        _platform = os.uname()[0]
        if _platform == 'Linux':
            prefix = os.path.join('/', 'fs0')
        else:
            prefix = os.path.join(os.path.expanduser('~'), 'Code', 'eprime2redcap')
        return prefix

    def split_fname(self):
        bname = os.path.basename(self.fname)
        self.bname = bname
        name, ext = os.path.splitext(bname)
        parts = name.split('_')
        try:
            self.project = parts[0]
            self.task = parts[1]
            self.behavid = parts[2]
            self.scanid = parts[3]
        except IndexError:
            raise ValueError("Poorly named file :(")
        return parts

    def parse_fname(self):
        """ Populate information from file name """
        self.split_fname()

    def key_map(self):
        """ Return a function transforming raw keys to RC fields """
        raise NotImplementedError

    def copy_fname(self):
        """ Return the path to where the copy should go """
        if not os.path.isdir(self.copy_dir):
            os.makedirs(self.copy_dir)
        return os.path.join(self.copy_dir, self.bname + '.txt')

    def parse(self):
        """ Parse the file and return redcap-able results """
        func = self.parsers[self.task]
        data = func(self.fobj, self.copy_fname())
        key_map = self.key_map()
        to_redcap = {}
        for k, v in data.items():
            to_redcap[key_map(k)] = v
        #  Update to_redcap with project specific dicta
        to_redcap.update(self.project_additions())
        return to_redcap

    def upload_key(self):
        """ Returns a key for the in-magnet database that can be used to check
        for previous uploads """
        return None

    def project_additions(self):
        """ Return a new dictionary with key/values not inserted by any particular
        parser but that need to be in data for redcap """
        raise NotImplementedError


class LERDLMS(BaseProject):
    def __init__(self, fname, fobj, database='in-magnet'):
        super(LERDLMS, self).__init__(fname, fobj, database)
        self.parsers = {"SRT": pf.LERD_SRT, "PIC2": pf.NF_PIC}
        self.copy_dir = os.path.join(self.prefix(),
                                     'New_Server',
                                     'LERDLMS',
                                     'In_Behavioral',
                                     '%s_%s' % (self.behavid, self.scanid))

    def parse_fname(self):
        self.split_fname()

    def key_map(self):
        if self.task == 'SRT':
            return lambda x: 'srt_%s' % x
        elif self.task == 'PIC2':
            return lambda x: 'picturev2_%s' % x
        else:
            return lambda x: x

    def project_additions(self):
        return {'id': '%s_%s' % (self.behavid, self.scanid)}


class LERDP2I(BaseProject):
    """Imaging Files"""

    def __init__(self, fname, fobj, database='in-magnet'):
        super(LERDP2I, self).__init__(fname, fobj, database)
        self.parsers = {"SRT": pf.LERD_SRT, 'PIC2': pf.NF_PIC}
        self.copy_dir = os.path.join(self.prefix(),
                                     'New_Server',
                                     'LERDP2',
                                     'In_Behavioral',
                                     '%s_%s' % (self.behavid, self.scanid))

    def parse_fname(self):
        self.split_fname()

    def key_map(self):
        if self.task == 'SRT':
            return lambda x: 'srt_%s' % x
        elif self.task == 'PIC2':
            return lambda x: 'picturev2_%s' % x
        else:
            return lambda x: x

    def project_additions(self):
        return {'id': '%s_%s' % (self.behavid, self.scanid)}


class LERDP2(BaseProject):
    """Behavioral files"""
    parsers = {"DLPICENC": pf.LERDP2B_DLPICENC,
               "DLPICREC": pf.LERDP2B_DLPICREC,
               "DLWORDENC": pf.LERDP2B_DLWORDENC,
               "DLWORDREC": pf.LERDP2B_DLWORDREC,
               "DLWORDRET": pf.LERDP2B_DLWORDRET,
               "SRT2": pf.RCVB_SRT,
               "SRT": pf.RCVB_SRT,
               'OLSON': pf.LERDP2_OLSON,
               'SYM': pf.LERDP2_PRICE_SYM,
               'NONSYM': pf.LERDP2_PRICE_NONSYM}

    def __init__(self, fname, fobj, database='lerdp2'):
        super(LERDP2, self).__init__(fname, fobj, database)
        self.copy_dir = os.path.join(self.prefix(),
                                     'New_Server',
                                     'LERDP2',
                                     'Out_Behavioral',
                                     'Longitudinal',
                                     'Behavioral Participant Folders',
                                     'LERD_P2_%s' % self.behavid,
                                     '_'.join(['LERD_P2', self.behavid, 'E-Prime']))

    def split_fname(self):
        """Fancy split_fname"""
        bname = os.path.basename(self.fname)
        self.bname = bname
        name, ext = os.path.splitext(bname)
        parts = name.split('_')
        try:
            self.project = parts[0]
            self.task = parts[1]
            self.behavid = parts[2]
            self.visit = parts[3]
        except IndexError:
            raise ValueError("Poorly named file :(")
        return parts

    def project_additions(self):
        to_add = {'participant_id': self.behavid}
        return to_add

    def key_map(self):
        if self.task in ("DLPICENC", "DLPICREC", "OLSON",
                         "DLWORDENC", "DLWORDREC", "DLWORDRET", "SYM",
                         "NONSYM"):
            f = lambda x: '%s_%s' % (self.visit.lower(), x)
        elif self.task in ('SRT2', "SRT"):
            f = lambda x: '%s_srtb_%s' % (self.visit.lower(), x)
        else:
            f = lambda x: x
        return f


class NF(BaseProject):

    def __init__(self, fname, fobj, database='in-magnet'):
        super(NF, self).__init__(fname, fobj, database)
        self.rcmap = {'SWR': 'swr1', 'MI': 'mi1', 'REP': 'rep1', 'PIC': 'pic1'}
        self.parsers = {'SWR': pf.NF_SWR, 'MI': pf.NF_MI, 'REP': pf.NF_REP, 'PIC': pf.NF_PIC}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'NF',
                            'In_Behavioral', '_'.join([self.behavid, self.scanid]))
        self.parse_fname()

    def parse_fname(self):
        self.split_fname()

    def project_additions(self):
        return {'grant': self.project, 'id': '%s_%s' % (self.behavid, self.scanid)}

    def key_map(self):
        return lambda x: '%s_%s' % (self.rcmap[self.task], x)


class RCK(BaseProject):
    def __init__(self, fname, fobj, database='in-magnet'):
        super(RCK, self).__init__(fname, fobj, database)
        self.rcmap = {'SWR': 'swr2'}
        self.parsers = {'SWR': pf.RCK_SWR}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'RCK', 'In_Behavioral', '_'.join([self.behavid, self.scanid]))
        self.parse_fname()

    def project_additions(self):
        return {'id': '_'.join([self.behavid, self.scanid]), 'grant': 'RCK'}

    def split_fname(self):
        bname = os.path.basename(self.fname)
        self.bname = bname
        name, ext = os.path.splitext(bname)
        parts = name.split('_')
        try:
            self.project = parts[0]
            self.task = parts[1]
            self.behavid = parts[2]
            self.scanid = parts[3]
        except IndexError:
            raise ValueError("Poorly named file :(")
        return parts

    def key_map(self):
        return lambda x: '%s_%s_%s' % (self.rcmap[self.task], 'pre', x)


class NFB(BaseProject):

    def __init__(self, fname, fobj, database='nf'):
        super(NFB, self).__init__(fname, fobj, database)
        self.parsers = {'OLSON': pf.NFB_OLSON, 'MI': pf.NFB_MI, 'MR': pf.NFB_MR,
                        'SENT': pf.NFB_SENT, 'FIG': pf.NFB_FIG}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'NF',
                            'Out_Behavioral', '_'.join([self.behavid, self.scanid]))

    def parse_fname(self):
        parts = self.split_fname()
        try:
            if self.task in ('FIG', 'MI', 'MR', 'OLSON'):
                self.visit = parts[4]
        except IndexError:
            raise ValueError("Poorly named file :(")

    def key_map(self):
        if hasattr(self, 'visit'):
            if self.visit == 'Pre':
                visit = '1'
            else:
                visit = '2'
            key_map = lambda x: x.replace('X', visit)
        else:
            key_map = lambda x: x
        return key_map

    def project_additions(self):
        return {'studyid': self.behavid}


class RCV(BaseProject):
    def __init__(self, fname, fobj, database='in-magnet'):
        super(RCV, self).__init__(fname, fobj, database)
        self.parsers = {'PASSAGES': pf.RCV_PASSAGES_NEW}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'RCV',
            'In_Behavioral', '_'.join([self.behavid, self.scanid]))

    def parse_fname(self):
        self.split_fname()

    def key_map(self):
        if self.task == 'PASSAGES':
            return lambda x: 'passagesv2_%s' % x
        else:
            return lambda x: x

    def project_additions(self):
        return {'id': '_'.join([self.behavid, self.scanid])}


class RCVB(BaseProject):

    def __init__(self, fname, fobj, database='rc'):
        super(RCVB, self).__init__(fname, fobj, database)
        self.parsers = {'SENT': pf.NFB_SENT, 'DLPICENC': pf.LERDP2B_DLPICENC,
                        'DLPICREC': pf.LERDP2B_DLPICREC, 'SRT': pf.RCVB_SRT}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'RCV',
                            'Out_Behavioral', 'RC_%s' % self.behavid, 'RC_%s_E-Prime' % self.behavid)

    def parse_fname(self):
        self.split_fname()

    def key_map(self):
        if self.task == 'SRT':
            return lambda x: 'srtb_%s' % x
        else:
            return lambda x: x

    def project_additions(self):
        return {'participant_id': '_'.join([self.behavid, self.scanid])}


class LERDB(BaseProject):

    def __init__(self, fname, fobj, database='lerd'):
        super(LERDB, self).__init__(fname, fobj, database)
        self.parsers = {'OLSON': pf.NFB_OLSON}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'LERD',
                            'Out_Behavioral', '_'.join([self.behavid, self.scanid]))

    def parse_fname(self):
        self.split_fname()

    def project_additions(self):
        return {'participant_id': '_'.join([self.behavid, self.scanid])}

    def key_map(self):
#         mapper = {'otXtc': 'olson_total_correct', 'otXcmrt': 'olson_correct_mean',
#                 'otXcsdrt': 'olson_correct_sd', 'otXimrt': 'olson_incorrect_mean',
#                 'otXisdrt': 'olson_incorrect_sd'}
#         return lambda x: mapper[x]
        #  LERD database changed?
        return lambda x: x.replace('X', '1')


class LDRC1(BaseProject):
    def __init__(self, fname, fobj, database='in-magnet'):
        super(LDRC1, self).__init__(fname, fobj, database)
        self.parsers = {'NBACK': pf.LDRC1_NBACK, 'SENT': pf.LDRC1_SENT}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'LDRC1',
                            'In_Behavioral', self.behavid)

    def split_fname(self):
        """ This needs a fancy split_fname because there's no scanid """
        bname = os.path.basename(self.fname)
        self.bname = bname
        name, ext = os.path.splitext(bname)
        parts = name.split('_')
        try:
            self.project = parts[0]
            self.task = parts[1]
            self.behavid = parts[2]
        except IndexError:
            raise ValueError("Poorly named file :(")
        return parts

    def parse_fname(self):
        self.split_fname()

    def project_additions(self):
        to_add = {'id': self.behavid, 'grant': 'LDRC1'}
        task = self.task.lower()
        if task == 'nback':
            task = 'nback1'
        elif task == 'sent':
            task = 'sent1'
        to_add['%s_upload' % task] = 'yes'
        return to_add

    def key_map(self):
        if self.task == 'NBACK':
            f = lambda x: 'nback1_%s' % x
        elif self.task == 'SENT':
            f = lambda x: 'sent1_%s' % x
        return f


class RCLMS(BaseProject):
    def __init__(self, fname, fobj, database='in-magnet'):
        super(RCLMS, self).__init__(fname, fobj, database)
        self.parsers = {'PASSAGES': pf.RCV_PASSAGES}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'RC_LMS',
                                     'In_Behavioral', '%s_%s' % (self.behavid, self.scanid))

    def key_map(self):
        if self.task == "PASSAGES":
            return lambda x: 'passagesv2_%s' % x
        else:
            return lambda x: x

    def project_additions(self):
        return {'id': '%s_%s' % (self.behavid, self.scanid),
                'grant': "RC_LMS"}


class ARN(BaseProject):
    def __init__(self, fname, fobj, database='in-magnet'):
        super(ARN, self).__init__(fname, fobj, database)
        self.parsers = {'Rep': pf.ARN_REP}
        self.copy_dir = os.path.join(self.prefix(), 'New_Server', 'ARN',
                            'In_Behavioral', self.behavid)

    def parse_fname(self):
        self.split_fname()

    def project_additions(self):
        to_add = {'id': '_'.join([self.behavid, self.scanid]), 'grant': 'ARN', 'rep2_upload': 'yes'}
        return to_add

    def key_map(self):
        return lambda x: 'rep2_%s' % x
