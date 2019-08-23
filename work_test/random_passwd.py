import string,random

write_passwd = open('E:\\my_python\\my_learning\\dst\\passwd.txt','w+')
for i in range(1,10):
  def random_num(randomlength=8):
    a = list(map(lambda x:random.choice(string.digits), range(8)))
    random.shuffle(a)
    return ''.join(a[:randomlength])
  passwd = random_num(8)
  print (passwd)
  line = passwd  +'\n'
  write_passwd.writelines(line)
