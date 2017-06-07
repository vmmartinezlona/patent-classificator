#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:32:30 2017

@author: tsukimo
"""

from os import walk, path
import re

def ls(regex = '.xml', route = '/home/jaime/BACKUP/Docs/DataMining/project/wipo-alpha/train'):
    pat = re.compile(regex, re.I)
    result = []
    for (dir, _, files) in walk(route):
        result.extend([ path.join(dir,arch) for arch in
                              filter(pat.search, files) ])
    return result


files = ls()
f = open("routes.txt", "w")
for file in files:
    f.write(file+'\n')

mainDir = './'
xmlDir = './test/'

newFile = mainDir + '/' + 'all_files.txt'


with open(newFile, 'w', encoding = 'UTF-8') as file:
    with open(mainDir + 'routes.txt') as f:
        for line in f:
            path = line[:-1]
            with open(path, encoding = 'iso-8859-1') as content_file:
                content = content_file.read()
                file.write(content)
                file.write('\n')
