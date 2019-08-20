#coding=utf-8
import subprocess,os,sys

clear = open('E:\\my_python\\my_test\\dst_files\\dst.txt','w')
clear.close()

src_file = 'E:\\my_python\\my_test\\src_files\\src.txt'
tmp_file = 'E:\\my_python\\my_test\\dst_files\\tmp.txt'

src = open(src_file,'r+')

def ping(url):
    dst_file = 'E:\\my_python\\my_test\\dst_files\\dst.txt'
    dst = open(dst_file,'a+')
    cmd = 'ping -n 1 ' + url
    cmd1 = 'ipconfig'
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for l in output.stdout.readlines():
        line = l.decode('gb2312')
        if "[" in line:
            ip = line.split('[')[1].split(']')[0]
            newline = url.strip() + '\t\t' + ip + '\n'
            print (newline)
            dst.write(newline)
            dst.close()

for url in src.readlines():
    ping(url)
