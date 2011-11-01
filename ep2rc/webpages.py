#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os
import string

import web
import re
import base64


import core
import rc
from config import cfg

temp_dir = os.path.join(os.path.split(__file__)[0], 'templates')
render = web.template.render(temp_dir)

allowed = cfg.items('users')

user = ''
sub_info = {}

available_grants = ['']
available_grants.extend(core.GRANTS)
subject_form = web.form.Form(
    web.form.Textbox('user', description="Your name", value=user),
    web.form.Textbox('id', description="Unique subject ID"),
    web.form.Dropdown(name='grant', args=available_grants, value=''),
    web.form.Textbox('task', description="Task"),
    web.form.Textbox('visit', description="Visit"),
    web.form.Textbox('list', description="List"),
    web.form.Button('submit', type='submit', description="Go to upload page")
)


class Upload:
    def GET(self):
        key = core.upload_key(sub_info)
        p = rc.previous_upload(sub_info['id'], key)
        return render.upload(p)
        
    def POST(self):
        x = web.input(myfile={})
        
        #  Parse!
        to_redcap = core.parse_file(x['myfile'].filename, x['myfile'].file)
        success = rc.upload(to_redcap)
        res = 0
        if success:
            res = 1
            sub_info = {}
        return render.results(res, to_redcap)


class Index:
    def GET(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
            f = subject_form()
            return render.subject_form(f)
        else:
            raise web.seeother('/login')
    
    def POST(self):
        f = subject_form()
        if not f.validates():
            pass    
        else:
            to_log = ('user', 'id', 'grant', 'task', 'visit', 'list')
            for k in to_log:
                sub_info[k] = f[k].get_value()
            print sub_info
            raise web.seeother('/upload')

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            username,password = base64.decodestring(auth).split(':')
            if (username,password) in allowed:
                user = username
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return
