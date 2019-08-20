#coding:UTF-8
import requests,sys

login_url = 'http://192.168.1.209:8888/admin/login.pl'
arp_url = 'http://192.168.1.209:8888/admin/info_arpcache.pl'

#imp.reload(sys)
session = requests.session()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
data = {"loginid":"xiezhenkun", "passwd":"29ab20c716a35cb80722617ee355227c","save":"on","ok":"登录"}
session.post(login_url, data = data)
response = session.get(arp_url)



temp1 = 'C:\\Users\\Administrator\\Desktop\\temp1.txt'
temp2 = 'C:\\Users\\Administrator\\Desktop\\temp2.txt'
w1 = open(temp1,'w')
w1.write(str(response.text.encode('utf8')))
w1.close()
print (response.text)
r1 = open(temp1,'r')
w2 = open(temp2,'w')
for line in r1.readlines():
    if re.search(keywords,line) == None and len(line.split('<td>')) == 2 and re.search('</td>',line) != None and re.search('<td>\w+<\/td>',line) == None:
        newline = line.split('<td>')[1].split('</td>')[0].replace('&nbsp;','')
        if re.search('-',newline) == None:
            w2.write(newline + '\t\t')
        else:
            w2.write(newline + '\n')
w2.close()






for i in temp1,temp2:
    os.remove(i)
