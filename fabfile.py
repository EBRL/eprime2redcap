#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

from fabric.api import run, cd, env, hosts, local, settings, lcd, prefix

env.hosts = ['cutting.accre.vanderbilt.edu']
env.user = 'burnsss1'
activate = 'source ~/envs/switchboard/bin/activate'
code_dir = '/home/burnsss1/Code/eprime2redcap'
supervisor_dir = '/home/burnsss1/supervisord/'


def rebuild():
    clean()
    local("python setup.py develop -u")
    local("python setup.py clean")
    local("python setup.py install")
    clean()


def clean():
    local("""find ep2rc/ -type f -name "*.pyc" -exec rm {} \;""")
    local("rm -rf build")
    local("rm -rf dist")
    local("rm -rf Eprime2Redcap.egg-info")


def check():
    with settings(warn_only=True):
        local("pyflakes ep2rc/ bin/*.py")
        local("pep8 ep2rc/ bin/*.py --ignore E501")


def test():
    local('nosetests -w test/')


def deploy(branch='master'):
    with cd(code_dir):
        run('git pull origin %s' % branch)
    with prefix(activate):
        with cd(code_dir):
            run('python setup.py install')
        with cd(supervisor_dir):
            run('supervisorctl restart switchboard:*')