#!/usr/bin/python
# -*- coding: UTF-8 -*-
file = open('c:\\dnslist.txt','r')
tempfile = open('c:\\test.txt','w+')
output = ''

for line in file.readlines():
    if(line.find('CNAME')!=-1):
        output += line
        #print line
    else:
        #output += line
        pass

tempfile.write(output)