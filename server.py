#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string
import pprint

import web
from web import form
import re
import base64

import eprime2redcap as ep2rc

with open(os.path.expanduser('~/.ep2rc.cfg')) as f:
    allow_raw = f.readlines()
allow_raw[:] = map(string.strip, allow_raw)
allowed = [(l.split(':')[0], l.split(':')[1]) for l in allow_raw]


urls = (
    '/','Index',
    '/login','Login',
    '/upload', 'Upload'
)

app = web.application(urls, globals())

render = web.template.render('templates')

subject_form = form.Form(
    form.Textbox('user', description="Your name"),
    form.Textbox('id', description="Unique subject ID"),
    form.Dropdown(name='grant', args=['', 'NF', 'RCV', 'LERD'], value=''),
    form.Textbox('task', description="Task"),
    form.Textbox('visit', description="Visit"),
    form.Textbox('list', description="List"),
    form.Button('submit', type='submit', description="Go to upload page")
)

class Upload:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        
        #  Parse!
        to_redcap = ep2rc.parse_file(x['myfile'].filename, x['myfile'].file)
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pformat(to_redcap)


class Index:
    def GET(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
            #  do $:f.render() in the template
            f = subject_form()
            return render.subject_form(f)
        else:
            raise web.seeother('/login')
    
    def POST(self):
        f = subject_form()
        if not f.validates():
            return render.subject_form(f)
        else:
            to_log = ('user', 'id', 'grant', 'task', 'visit', 'list')
            print ' '.join(['%s:%s' % (lf, f[lf].get_value()) for lf in to_log])
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
                raise web.seeother('/upload')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return

if __name__=='__main__':
    app.run()