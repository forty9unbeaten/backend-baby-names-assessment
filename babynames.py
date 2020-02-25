#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse


def extract_names(filename):
    names = []

    birth_year = re.findall(r'\d+', filename)[0]
    names.append(birth_year)

    with open(filename, 'r') as file:
        reg_ex = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
        ranked_names = re.findall(reg_ex, file.read())

    for name_tup in ranked_names:
        boy_name = name_tup[1]
        girl_name = name_tup[2]
        name_rank = str(name_tup[0])

        if boy_name not in ' '.join(names):
            names.append(boy_name + ' ' + name_rank)
        if girl_name not in ' '.join(names):
            names.append(girl_name + ' ' + name_rank)

    return sorted(names)


def create_parser():
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):

    # Implement command-line parser
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files
    create_summary = ns.summaryfile

    # Get names list for all files supplied and either print to shell or
    # write summary file
    for file in file_list:
        names = '\n'.join(extract_names(file)) + '\n'
        if create_summary:
            output_file = file + '.summary'
            with open(output_file, 'w') as summary_file:
                summary_file.write(names)
        else:
            print(names)


if __name__ == '__main__':
    main(sys.argv[1:])
