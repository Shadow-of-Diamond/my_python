from collections import Counter
import re

file = 'C:\\Users\\Administrator\\Desktop\\ip_up.txt'
r_file = open(file,'r')
arp_list = []

for line in r_file.readlines():
    if len(line.split()) > 2:
        ip = line.split()[0]
        mac = line.split()[1]
        des = line.split()[2]
        arp_list.append(ip + '\t\t' + mac + '\t\t' + des)
    elif len(line.split()) == 2:
        ip = line.split()[0]
        mac = line.split()[1]
        arp_list.append(ip + '\t\t' + mac + '\t\t ')


r_file.close()
#print (arp_list[1].split()[0])

for i in range(len(arp_list)):
    ip = arp_list[i].split()[0]
    mac = arp_list[i].split()[1]
    if len()

#print (arp_list)

#ip_up = []
#
#if len(ip_list) == len(mac_list) == len(des_list):
#    for key,value in dict(Counter(ip_list)).items():
#        print (key,value)
#        if value != 1:
#            #print (key)
#            ip_up.append(key)
#
#print (ip_up)
#mac_check_list = []
#
#r_file = open(file,'r')
#for line in r_file.readlines():
#    ip = line.split()[0]
#    mac = line.split()[1]
#    for i in ip_up:
#        if re.search(i,line) != None:
#            mac_check_list.append(mac)
#        print (len(set(mac_check_list)))
##            if len(mac_check_list) != set(len(mac_check_list)):
##                print ('have duplicates!!!')