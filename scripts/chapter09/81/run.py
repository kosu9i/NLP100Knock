#!/usr/bin/env python2
# coding: utf-8

import sys
import argparse
import re
import lxml.html
import requests


def get_country_name_list(args):
    country_name_list = []

    if args.country_name_list is not None:
        for line in args.country_name_list:
            country_name_list.append(line.strip())
    else:
        target_url = 'http://www6.kaiho.mlit.go.jp/isewan/image/flags/_flags.htm'
        html = requests.get(target_url).text
        root = lxml.html.fromstring(html)
        trs = root.xpath('//table/tbody/tr')
        for tr in trs:
            tds = tr.xpath('td')
            for i, td in enumerate(tds):
                if i != 2: continue 

                country_name = td.text
                m = re.search(ur'(.+)\((.+)\)', country_name)
                if m is not None:
                    for c in  m.groups():
                        country_name_list.append(c)
                else: 
                    country_name_list.append(td.text)
        with open('./country_name_list.txt', 'w') as f:
            f.write('\n'.join(country_name_list))
    
    return country_name_list
    

def convert_country_name(args):
    country_name_list = get_country_name_list(args) 

    for line in args.input_file:
        line = line.strip()
        if line == '':
            args.output_file.write('\n')
            continue

        for country_name in country_name_list:
            line = line.replace(country_name, country_name.replace(' ', '_'))

        args.output_file.write(line + '\n')


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',  type=argparse.FileType('r'), nargs='?',
                        default='../80/enwiki-20150112-400-r100-10576.txt')
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?',
                        default='./enwiki-20150112-400-r100-10576.txt')
    parser.add_argument('-c', dest='country_name_list', default=None)
    return parser.parse_args()

def main():
    args = arg_parse()
    convert_country_name(args)

if __name__ == '__main__':
    main()

