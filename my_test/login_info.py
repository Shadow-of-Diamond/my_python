#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

tmp = open('f:\\python_test\\login_tmp.txt', 'w')
with open('f:\\python_test\\log.txt', 'r') as f:
    for line in f.readlines():
        if re.search(r'20[1-9][1-9]$',line) != None:
#           tmp.write(line)
            time = line
        elif re.search(r'User-Name', line) != None:
#           tmp.write(line)
            name = line
        elif re.search(r'Calling-Station-Id', line) != None:
#           tmp.write(line)
            mac = line
        elif re.search('^$', line) != None:
#           tmp.write(line)
            black = line




login_info = [time, name, mac,black]
tmp.close()


#print (login_info)
