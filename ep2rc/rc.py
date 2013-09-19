#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


from redcap import Project

from config import pname_keys


def get_project(pname, url='https://redcap.vanderbilt.edu/api/'):
    return Project(url, pname_keys[pname])


def upload(to_upload, pname='in-magnet'):
    """ Upload a dictionary to a Redcap database

    Parameters
    ----------
    to_upload: dict
        Dictionary of data to upload
    pname: str
        project name that defines to which project data will be uploaded
    Returns
    -------
    success: bool
        False on failure
    """
    project = get_project(pname.lower())
    data = [to_upload]
    response = project.import_records(data)
    if 'error' in response:
        print("Upload failed: %s" % response['error'])
        return False
    if 'count' in response and response['count'] != len(data):
        print("Upload failed: len(data)=%d and response['count']=%s" %
            (len(data), response['count']))
        success = False
    else:
        success = True
    return success


def previous_upload(id, key, pname='in-magnet'):
    project = get_project(pname.lower())
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
