#coding:utf-8

import string,random,threading,time
write_passwd = open('E:\\my_python\\my_learning\\dst\\passwd.txt','w+')

def random_num(randomlength=8):
  a = list(map(lambda x:random.choice(string.digits), range(8)))
  random.shuffle(a)
  mypasswd = ''.join(a[:randomlength])
  print (mypasswd)
  write_passwd.write(mypasswd+'\n')
#  return mypasswd


for i in range(0,5):
  passwd = threading.Thread(target=random_num(8))
  passwd.start()