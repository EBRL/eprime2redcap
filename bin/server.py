#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import web

from ep2rc.webpages import *

def is_test():
    testing = False
    if 'WEBPY_ENV' in os.environ:
        testing = os.environ['WEBPY_ENV'] == 'test'
    return testing
    
    
urls = (
    '/','Index',
    '/login','Login',
    '/upload/(.*)', 'Upload'
)

app = web.application(urls, globals())


if (not is_test()) and __name__=='__main__':
    app.run()