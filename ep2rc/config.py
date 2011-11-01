#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os
from ConfigParser import ConfigParser

platform = os.uname()[0]
if platform == 'Linux':
    prefix = '/fs0/'
else:
    prefix = os.path.expanduser('~')
ep2rc_cfg = os.path.join(prefix, '.ep2rc.cfg')

cfg = ConfigParser()
with open(ep2rc_cfg) as f:
    cfg.readfp(f)
