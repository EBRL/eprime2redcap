#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os
import ep2rc

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if __name__ == '__main__':

    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')
    
    long_desc = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read()

    setup(name='Eprime2Redcap',
        maintainer='Scott Burns',
        maintainer_email='scott.s.burns@gmail.com',
        description="""Eprime2Redcap: A simple web application for importing E-prime data to Redcap""",
        license='BSD (3-clause)',
        url='http://github.com/sburns/eprime2redcap',
        version=ep2rc.__version__,
        download_url='http://github.com/sburns/eprime2redcap/',
        long_description=long_desc,
        packages=['ep2rc'],
        package_data={'ep2rc': ['templates/*.html']},
        requires=['web.py', 'pycap'],
        platforms='any',
        classifiers=(
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved',
                'Topic :: Software Development',
                'Topic :: Scientific/Engineering',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX',
                'Operating System :: Unix',
                'Operating System :: MacOS',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.7',)
        )
