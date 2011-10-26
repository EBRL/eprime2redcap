#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os
from ConfigParser import ConfigParser

from redcap import Project

platform = os.uname()[0]
if platform == 'Linux':
    prefix = '/fs0/'
else:
    prefix = os.path.expanduser('~')
pycap_cfg = os.path.join(prefix, '.pycap.cfg')

cfg = ConfigParser()
with open(pycap_cfg) as f:
    cfg.readfp(f)
KEY = cfg.get('keys', 'In-Magnet')
del cfg

URL = 'https://redcap.vanderbilt.edu/api/'

project = Project(URL, KEY)

def upload(to_upload):
    """ Upload a dictionary to the In-Magnet database 
    
    Parameters
    ----------
    to_upload: dict
        Dictionary of data to upload
        
    Returns
    -------
    success: bool
        False on failure
    """
    data = [to_upload]
    print("Uploading...")
    num_uploaded = project.import_records(data)
    if num_uploaded != len(data):
        print("Upload failed")
        success = False
    else:
        print("Upload succeeded")
        success = True
    return success
    
def previous_upload(id, key):
    d = project.export_records(records=[id], fields=[key])
    if len(d) > 1:
        raise ValueError("Received results from multiple subjects")
    elif len(d) == 1:
        to_return = d[0][key] == 'yes'
    elif len(d) == 0:
        to_return = False
    else:
        to_return = False
    return to_return