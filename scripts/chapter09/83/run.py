#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',  type=argparse.FileType('r'), nargs='?',
                        default='../82/enwiki-20150112-400-r100-10576_context.tsv')
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?',
                        default='')
    return parser.parse_args()

def main():
    args = arg_parse()

if __name__ == '__main__':
    main()

