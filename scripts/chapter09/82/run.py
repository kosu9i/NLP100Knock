#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse
import random

def extract_context_words(args):

    random.seed(1)

    for line in args.input_file:
        line = line.strip()
        if line == '': continue

        word_list = line.split()

        for i, t in enumerate(word_list):
            d = random.randint(1,5)
            d_head = max(0, i - d)
            d_tail = min(len(word_list), i + d + 1)

            args.output_file.write('\t'.join([t,
                                              ' '.join(word_list[d_head:i]),
                                              ' '.join(word_list[i+1:d_tail])]) + '\n')

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',  type=argparse.FileType('r'), nargs='?',
                        default='../81/enwiki-20150112-400-r100-10576.txt')
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?',
                        default='./enwiki-20150112-400-r100-10576_context.tsv')
    return parser.parse_args()

def main():
    args = arg_parse()
    extract_context_words(args)
    

if __name__ == '__main__':
    main()

