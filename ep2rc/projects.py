#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

class BaseProject(object):
    """ Base class from which all Projects should inherit"""
    
    def __init__(self):
        """ Constructor """
        
        self.behav = False
        