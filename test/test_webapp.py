#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

from paste.fixture import TestApp
from nose.tools import *

from server import app

class TestCode():
    def setup(self):
        mw = []
        return TestApp(app.wsgifunc(*mw))

    def test_index(self):
        testApp = self.setup()
        r = testApp.get('/')
        assert_equal(r.status, 200)
        r.mustcontain('ep2rc')
    
    def test_upload(self):
        testApp = self.setup()
        r = testApp.get('/upload/')
        assert_raises('AttributeError', testApp.get, ['/upload/'])
    