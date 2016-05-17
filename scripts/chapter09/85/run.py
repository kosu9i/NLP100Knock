#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse
import copy
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import TruncatedSVD

def pca(args):
    context_dic = {}
    word_dic = {}
    keylist = []
    vector_list=[]

    for line in args.input_file:
        t, c, Xtc = line.strip().split('\t')

        context_dic[c]=Xtc #二重辞書化
        if t in word_dic:
            word_dic[t].update(context_dic)
        else:
            word_dic[t] = context_dic
        context_dic={}
   
    for t, cont in word_dic.items(): #リスト化
        keylist.append(t)
        vector_list.append(cont)

    vec = DictVectorizer(sparse=True)
    array_vectors = vec.fit_transform(vector_list)
    tsvd = TruncatedSVD(n_components=300)
    word_pca = tsvd.fit_transform(array_vectors)

    n=0
    while n < len(keylist):
        args.output_file.write(keylist[n])
        args.output_file.write(" ")
        for m in word_pca[n]:
            precision = 6
            m = str(np.round(m, precision))
            args.output_file.write(m)
            args.output_file.write(" ")
        n += 1
        args.output_file.write("\n")


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',  type=argparse.FileType('r'), nargs='?',
                        default='../84/context_matrix.tsv')
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?',
                        default='pca.tsv')
    return parser.parse_args()

def main():
    args = arg_parse()
    pca(args)

if __name__ == '__main__':
    main()

