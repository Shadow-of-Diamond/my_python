#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os , commands


#pcvideo = 'db.pcvideo.com.cn'
#pcvideo_new = pcvideo+'.new'
#
#f_pcvideo = fpath + pcvideo
#f_pcvideo_new = fpath + pcvideo_new
#os.popen("touch "+f_pcvideo_new)
#
#file_pcvideo=open(f_pcvideo,'r+')
#newfile_pcvideo=open(f_pcvideo_new,'r+')
#lines = file_pcvideo
#for line in lines:
#    if line.find('192.168.52.') != -1 or line.find('192.168.53.') != -1:
#        if line.split()[2] == 'A':
#            if line.startswith('t'):
#                newline = 't-'+line[1:]
#                print newline
#                newfile_pcvideo.write(line.replace(line,newline))
#    else:
#        newfile_pcvideo.write(line)



#pc = 'db.pc.com.cn'
#pconline = 'db.pconline.com.cn'
#pcauto = 'db.pcauto.com.cn'
#pclady = 'db.pclady.com.cn'
#pcbaby = 'db.pcbaby.com.cn'
#pcvideo = 'db.pcvideo.com.cn'
#imofan = 'db.imofan.com'
#geeknev = 'db.geeknev.com'


path = '/var/named/chroot/var/named/'
files= os.listdir(path)
s = []
for file in files:
    if not os.path.isdir(file):
        f = open(path+"/"+file,'r');
        iter_f = iter(f); #历遍目录下的文件
        str = ""
        for line in iter_f:
            str = str + line
#            print line
#        s.append(str)
            if line.find('192.168.52.') != -1 or line.find('192.168.53.') != -1:
                if line.split()[2] == 'A':
                    if line.startswith('t'):
                        newline = 't-'+line[1:]
                        print newline
                        f.write(line.replace(line,newline))
    else:
        f.write(line)