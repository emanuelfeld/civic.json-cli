#! /usr/bin/env python
# -*- codes: utf-8 -*-

import sys
from .civicjson import add_template, validate_file


def usage():
    message = ("Usage:\n"
               "civicjson <subcommand>\n"
               "  Subcommands:\n"
               "\tinit\tInitialize a civic.json file in this directory\n"
               "\tvalidate\tValidate the civic.json file in this directory")
    print(message)


def main(args=sys.argv):
    args.pop(0)
    try:
        if args[0] == 'init':
            add_template()
        elif args[0] == 'validate':
            validate_file()
        else:
            usage()
    except:
        usage()
