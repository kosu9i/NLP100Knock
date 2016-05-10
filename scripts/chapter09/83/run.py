#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse
from datetime import datetime

def calc_frequency(args):
    tc_dict = {}
    t_dict = {}
    c_dict = {}
    for i, line in enumerate(args.input_file):
        t, c = line.strip().split('\t')

        tc_dict[(t, c)] = tc_dict.get((t, c), 0) + 1
        t_dict[t] = t_dict.get(t, 0) + 1
        c_dict[c] = c_dict.get(c, 0) + 1

        if i % 100000 == 0:
            print '{0} {1} lines processed.'.format(
                    datetime.now().strftime('%Y/%m/%d %H:%M:%S'), i)


    for (t, c), count in sorted(tc_dict.items()):
        args.ftc.write('\t'.join([t, c, str(count)]) + '\n')

    for t, count in sorted(t_dict.items()):
        args.ft.write('\t'.join([t, str(count)]) + '\n')

    for c, count in sorted(c_dict.items()):
        args.fc.write('\t'.join([c, str(count)]) + '\n')

    args.N.write(str(len(tc_dict))) 


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',  type=argparse.FileType('r'), nargs='?',
                        default='../82/enwiki-20150112-400-r100-10576_context.tsv')
    parser.add_argument('--ftc', dest='ftc', type=argparse.FileType('w'), 
                        default='./freq_tc.tsv')
    parser.add_argument('--ft', dest='ft', type=argparse.FileType('w'), 
                        default='./freq_t.tsv')
    parser.add_argument('--fc', dest='fc', type=argparse.FileType('w'), 
                        default='./freq_c.tsv')
    parser.add_argument('--N', dest='N', type=argparse.FileType('w'), 
                        default='./N.txt')
    return parser.parse_args()

def main():
    args = arg_parse()
    calc_frequency(args)

if __name__ == '__main__':
    main()

