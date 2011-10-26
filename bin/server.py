#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from ep2rc.webpages import *


urls = (
    '/','Index',
    '/login','Login',
    '/upload', 'Upload'
)

app = web.application(urls, globals())


if __name__=='__main__':
    app.run()