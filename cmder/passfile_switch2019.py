#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import string
import datetime

def escape_shift(character):
        if character == "1":
            return "!"
        elif character == "2":
            return "@"
        elif character == "3":
            return "#"
        elif character == "4":
            return '$'
        elif character == "5":
            return '%'
        elif character == "6":
            return "^"
        elif character == "7":
            return '&'
        elif character == "8":
            return "*"
        elif character == "9":
            return "("
        elif character == "0":
            return ")"
        else:
            pass

def threedigi(digi):
    if len(digi) == 3:
        return digi
    if len(digi) == 2:
        return '0'+ digi
    if len(digi) == 1:
        return '00'+ digi
def username(num):
    if num in ['232', '236', '237', '238', '239', '240', '241', '242', '243']:
        location = 'ct'
    elif num in ['224', '228', '229', '230', '231']:
        location = 'lt'
    elif num in ['1', '10', '11', '12', '13', '50']:
        location = 'gz'
    elif num in ['97', '90']:
        location = 'bj'
    elif num in ['197', '190']:
        location = 'sh'
    else:
        location = 'ot'
    return location

def switchpw(hosts):
    i = hosts.split('.')
    if '192.168' in hosts:
        if i[2] in ['232','236','237','238','239','240','241','242','243']:
            idc1 = 'c'
            idc2 = 't'
        elif i[2] in ['224','228','229','230','231']:
            idc1 = 'l'
            idc2 = 't'
        elif i[2] in ['1','10','11','12','13','50']:
            idc1 = 'g'
            idc2 = 'z'
        elif i[2] in ['97','90']:
            idc1 = 'b'
            idc2 = 'j'
        elif i[2] in ['197','190']:
            idc1 = 's'
            idc2 = 'h'
        else:
            idc1 = 'o'
            idc2 = 't'
        c = ""
        if int(i[3])%2 != 0:
            sum = threedigi(str(int(i[2]) + int(i[3])))
            for k in list(threedigi(str(i[3]))):
                c = c + escape_shift(k)
            pwd = idc1.lower() + c + idc2.upper() + sum
        else:
            sum = threedigi(str(int(i[2]) + int(i[3])))
            for k in list(threedigi(str(i[3]))):
                c = c + escape_shift(k)
            pwd = idc1.upper() + sum + idc2.lower() + c
        return pwd
    else:
        return 0

if __name__ == "__main__":
#    file_name = sys.argv[1]
    host_ip = sys.argv[1]
#    file_object = open(file_name)
    try:
#        for line in file_object.readlines():
        ip3 = host_ip.split('.')[2]
        ip4 = host_ip.split('.')[3]
        print (host_ip,' ',ip3+username(ip3)+ip4,' ',switchpw(host_ip))
#        for line in host_ip:
#            host_ip = line.split()[0]
#            ip3 = host_ip.split('.')[2]
#            ip4 = host_ip.split('.')[3]
#            print host_ip,' ',ip3+username(ip3)+ip4,' ',switchpw(host_ip)
    except:
        pass
#    file_object.close()

