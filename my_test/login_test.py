#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

tmp = open('f:\\python_test\\login_tmp.txt', 'w')
with open('f:\\python_test\\log.txt', 'r') as f:
    for line in f.readlines():
#        print (line.split()[5])
        if re.search(r'[0-9a-fA-F]{2}(-[0-9a-fA-F]{2}){5}',line.split()[5]) != None:
            name = line.split()[6]
            mac = line.split()[5]
            newline = line.split()[0]+' '+line.split()[1]+'  '+line.split()[2]+' '+line.split()[3]+' '+line.split()[4]+'\t'+name+'\t'+mac+'\t\n'
#            print (newline)
            tmp.write(newline)
        else:
            tmp.write(line)