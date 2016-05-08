#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse
import re

def clean_corpus(args):
    regex_del_sym_head = re.compile(ur'^[.,!?;:()\[\]\'"]+')
    regex_del_sym_tail = re.compile(ur'[.,!?;:()\[\]\'"]+$')

    for line in args.input_file:
        line = line.strip()
        if line == '':
            args.output_file.write('\n')
            continue

        token_list = []
        for token in  line.split():
            token.strip()
            token_u = token.decode('utf-8')
            token_u = regex_del_sym_head.sub('', token_u)
            token_u = regex_del_sym_tail.sub('', token_u)
            token = token_u.encode('utf-8')
            if token != '': token_list.append(token)

        args.output_file.write(' '.join(token_list) + '\n')


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',  type=argparse.FileType('r'), nargs='?',
                        default='../00/enwiki-20150112-400-r100-10576.txt')
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?',
                        default='enwiki-20150112-400-r100-10576.txt')
    return parser.parse_args()

def main():
    args = arg_parse()
    clean_corpus(args)

if __name__ == '__main__':
    main()

