#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import ep2rc

def arguments():
    import argparse
    ap = argparse.ArgumentParser()
    
    #  Arguments
    ap.add_argument('-f', dest='file',
        help='Parse and upload data from a (properly named) file')
    return ap.parse_args()


if __name__ == '__main__':
    args = arguments()

    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError("This file doesn't exist")
        with open(args.file) as f:
            to_redcap =  ep2rc.parse_file(args.file, f)
        ep2rc.upload(to_redcap)