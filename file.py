# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 02:55:41 2017

@author: erick
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
