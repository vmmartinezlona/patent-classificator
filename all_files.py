#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:32:30 2017

@author: tsukimo
"""

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
