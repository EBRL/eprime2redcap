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
    ap.add_argument('-f', dest='files', nargs='*',
        help='Parse and upload data from one (many) (properly named) file(s)')
    ap.add_argument('-d', dest='dir',
        help="Parse and upload all files from the given directory")
    ap.add_argument('--database', dest='database', default='in-magnet',
        help="Upload results to the given database")
    ap.add_argument('--no-upload', dest='upload', default=True, action='store_false',
        help='Do NOT upload information to redcap')
    return ap.parse_args()


if __name__ == '__main__':
    args = arguments()

    if args.files:
        for fname in args.files:
            if not os.path.isfile(fname):
                raise ValueError("This file doesn't exist")
            data, success = ep2rc.parse_and_upload(fname, args.database, args.upload)
            if not args.upload:
                print data

    if args.dir:
        if not os.path.isdir(args.dir):
            raise ValueError("This directory doesn't exist")
        all_txt = glob(os.path.join(args.dir, '*.txt'))
        print("Found %d txt files..." % len(all_txt))
        for txt in all_txt:
            bname = os.path.basename(txt)
            pattern = '(.*_){2,5}'
            if re.match(pattern, bname):
                data, success = ep2rc.parse_and_upload(txt, args.database, args.upload)
