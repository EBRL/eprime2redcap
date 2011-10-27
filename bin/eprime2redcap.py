#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import re
from glob import glob


import ep2rc

def arguments():
    import argparse
    ap = argparse.ArgumentParser()
    
    #  Arguments
    ap.add_argument('-f', dest='file',
        help='Parse and upload data from a (properly named) file')
    ap.add_argument('-d', dest='dir',
        help="Parse and upload all files from the given directory")
    return ap.parse_args()

def parse_and_upload(fname):
    with open(fname) as f:
        to_redcap = ep2rc.parse_file(fname, f)
    return ep2rc.upload(to_redcap)


if __name__ == '__main__':
    args = arguments()

    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError("This file doesn't exist")
        parse_and_upload(fname)
    if args.dir:
        if not os.path.isdir(args.dir):
            raise ValueError("This directory doesn't exist")
        all_txt = glob(os.path.join(args.dir, '*.txt'))
        files_to_parse = []
        for txt in all_txt:
            bname = os.path.basename(txt)
            pattern = '(.*_){3,5}'
            if re.match(pattern, bname):
                try:
                    if parse_and_upload(txt):
                        msg = "Success with %s"
                    else:
                        msg = "Failed with %s"
                except ep2rc.BadDataError:
                    msg = "Failed with %s"
                print msg % txt
                    
                    