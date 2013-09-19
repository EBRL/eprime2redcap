#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os as _os
from ConfigParser import ConfigParser as _CP

_platform = _os.uname()[0]
if _platform == 'Linux':
    _prefix = '/fs0/'
else:
    _prefix = _os.path.expanduser('~')
_ep2rc_cfg = _os.path.join(_prefix, '.ep2rc.cfg')

_cfg = _CP()
with open(_ep2rc_cfg) as _f:
    _cfg.readfp(_f)

""" Define usable data here so other files grab only what they need """

#  Usernames and passwords
user_pws = _cfg.items('users')
#  Redcap project names and API keys
pname_keys = {k:v for (k,v) in _cfg.items('rc')}
