import os
from ConfigParser import ConfigParser

import redcap


cfg = ConfigParser()
cfg.read([os.path.expanduser('~/pycap.cfg')])
KEY = cfg.get('keys', 'In-Magnet')

del cfg

URL = 'https://redcap.vanderbilt.edu/api/'

project = redcap.Project(URL, KEY)

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
    num_uploaded = project.import_records(data)
    success = True
    if num_uploaded != len(data):
        success = False
    return success