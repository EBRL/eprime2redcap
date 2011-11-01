#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os

from redcap import Project

from config import cfg
#  Instantiate all projects that ep2rc could use
projects = {}
for pname, key in cfg.items('rc'):
    projects[pname] = Project('https://redcap.vanderbilt.edu/api/', key)


def upload(to_upload, pname='in-magnet'):
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
    num_uploaded = projects[pname].import_records(data)
    if num_uploaded != len(data):
        print("Upload failed")
        success = False
    else:
        success = True
    return success
    
def previous_upload(id, key, pname='in-magnet'):
    d = projects[pname].export_records(records=[id], fields=[key])
    if len(d) > 1:
        raise ValueError("Received results from multiple subjects")
    elif len(d) == 1:
        to_return = d[0][key] == 'yes'
    elif len(d) == 0:
        to_return = False
    else:
        to_return = False
    return to_return