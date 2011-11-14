#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os
import string

import web
import re
import base64


from . import core
from . import rc
from . import config
from . import config

temp_dir = os.path.join(os.path.split(__file__)[0], 'templates')
render = web.template.render(temp_dir)

available_rc = [p[0] for p in config.pname_keys]

grants = ['']
grants.extend(core.GRANTS)
tasks = ['']
tasks.extend(core.TASKS)
visits = ['']
visits.extend(['Pre', 'Post'])

subject_form = web.form.Form(
    web.form.Textbox('user', description="Your name"),
    web.form.Textbox('id', description="Unique subject ID"),
    web.form.Dropdown(name='grant', args=grants, value=''),
    web.form.Dropdown(name='task', args=tasks, value=''),
    web.form.Dropdown(name='visit', args=visits, value=''),
    web.form.Textbox('list', description="List"),
    web.form.Radio('database', args=available_rc, value=''),
    web.form.Button('submit', type='submit', description="Go to upload page")
)
fields = ('user', 'id', 'grant', 'task', 'visit', 'list', 'database')

db = None

class Upload:
    def GET(self, *args):
        data = web.input()
        global db
        db = data.database
        info = {}
        for f in fields:
            info[f] = getattr(data, f)
        key = core.upload_key(info)
        if key:
            info['previous'] = rc.previous_upload(data.id, key, data.database)
        else:
            info['previous'] = False
        return render.upload(info)
        
    def POST(self, *args):
        x = web.input(myfile={})
        global db
        #  Parse
        to_redcap = core.parse_file(x['myfile'].filename, x['myfile'].file)
        success = rc.upload(to_redcap, db)
        res = 0
        if success:
            res = 1
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
            info = {}
            for k in fields:
                info[k] = f[k].get_value()
            url = '&'.join(['%s=%s' % (k,v) for k,v in info.items()])
            raise web.seeother('/upload/?%s' % url)

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            username,password = base64.decodestring(auth).split(':')
            if (username,password) in config.user_pws:
                user = username
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return
