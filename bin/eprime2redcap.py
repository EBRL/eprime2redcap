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
    ap.add_argument('--database', dest='database', default='in-magnet',
        help="Upload results to the given database")
    ap.add_argument('--no-upload', dest='upload', default=True, action='store_false',
        help='Do NOT upload information to redcap')
    return ap.parse_args()

def parse_and_upload(fname, database, do_upload=True):
    to_redcap = {}
    with open(fname) as f:
        to_redcap = ep2rc.parse_file(fname, f)
    suc = False
    if to_redcap and do_upload:
        suc = ep2rc.upload(to_redcap, database)
    return to_redcap, suc

if __name__ == '__main__':
    args = arguments()

    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError("This file doesn't exist")
        data, success = parse_and_upload(args.file, args.database, args.upload)
        if not args.upload:
            print data
    if args.dir:
        if not os.path.isdir(args.dir):
            raise ValueError("This directory doesn't exist")
        all_txt = glob(os.path.join(args.dir, '*.txt'))
        for txt in all_txt:
            bname = os.path.basename(txt)
            pattern = '(.*_){3,5}'
            if re.match(pattern, bname):
                try:
                    data, success = parse_and_upload(txt, args.database, args.upload)
                    if success:
                        msg = "Success with %s"
                    else:
                        msg = "Failed with %s"
                except ep2rc.BadDataError:
                    msg = "(BadDataError) Failed with %s"
                print msg % txt

