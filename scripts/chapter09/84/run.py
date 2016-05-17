#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse
import math
from datetime import datetime

def _read_freq(f, dict):
    for line in f:
        word, count = line.rstrip('\n').split('\t')
        dict.setdefault(word, int(count))

def create_context_matrix(args):
    N = int(args.N.readline().strip())
    t_dict, c_dict = ({}, {})

    _read_freq(args.ft, t_dict)
    _read_freq(args.fc, c_dict)

    for i, line in enumerate(args.ftc):
        t, c, count = line.rstrip('\n').split('\t')
        count = int(count)

        if i % 100000 == 0:
            print '{0} {1} lines processed.'.format(
                    datetime.now().strftime('%Y/%m/%d %H:%M:%S'), i)

        if count < 10: continue

        args.output_file.write('\t'.join([t, c,
            str(max(math.log(float(N * count) / (t_dict[t] * c_dict[c])), 0))]) + '\n')


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?',
                        default='./context_matrix.tsv')
    parser.add_argument('--ftc', dest='ftc', type=argparse.FileType('r'), 
                        default='../83/freq_tc.tsv')
    parser.add_argument('--ft', dest='ft', type=argparse.FileType('r'), 
                        default='../83/freq_t.tsv')
    parser.add_argument('--fc', dest='fc', type=argparse.FileType('r'), 
                        default='../83/freq_c.tsv')
    parser.add_argument('--N', dest='N', type=argparse.FileType('r'), 
                        default='../83/N.txt')
    return parser.parse_args()

def main():
    args = arg_parse()
    create_context_matrix(args)

if __name__ == '__main__':
    main()

