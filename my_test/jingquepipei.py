import re

key_words = "HSRP|00:00:00:00:00:00|flapping|LOGIN_SUCCESS|UPDOWN"
ign_words = "192.168.1.2\/192.168.1.2"

txt = 'E:\\my_python\\my_learning\\src\\sw_log.txt'
f = open(txt,'r')
for line in f.readlines():
    if re.search(key_words,line) != None:
#        print (line)
        if re.fullmatch(ign_words,line) != None:
            print (line)