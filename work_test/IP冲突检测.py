from collections import Counter
import re

file = 'C:\\Users\\Administrator\\Desktop\\1.txt'
r_file = open(file,'r')

ip_list = []
mac_list = []
des_list = []

for line in r_file.readlines():
    ip = line.split()[0]
    mac = line.split()[1]
    des = line.split()[3]
    ip_list.append(ip)
    mac_list.append(mac)
    des_list.append(des)
r_file.close()

#print (dict(Counter(ip_list)).values())
ip_up = []

if len(ip_list) == len(mac_list) == len(des_list):
    for key,value in dict(Counter(ip_list)).items():
#        print (key,value)
        if value != 1:
            #print (key)
            ip_up.append(key)

print (ip_up)
mac_check_list = []

r_file = open(file,'r')
for line in r_file.readlines():
    ip = line.split()[0]
    mac = line.split()[1]
    for i in ip_up:
        if re.search(i,line) != None:
            mac_check_list.append(mac)
        print (len(set(mac_check_list)))
#            if len(mac_check_list) != set(len(mac_check_list)):
#                print ('have duplicates!!!')