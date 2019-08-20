# -*- coding: UTF-8 -*-

import sys,requests,time

login_url = 'https://192.168.10.19/'
arp_url = 'https://192.168.10.19/diag_arp.php'

###  定义文件路径?Z
#arp_staff_data = arp_temp+'/arp_staff_'+today+'.txt'
#web_data = arp_temp+'/arp_web.txt'
#keywords = 'class|align|href'

###  重新加载系统，并定义编码为utf8?Z
reload(sys)
sys.setdefaultencoding('utf8')

###  创建session对象，可以保存Cookie
session = requests.session()

###  处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

###  需要登录的用户名和密码（密码已加密）
#data = {"usernamefld":"xiezhenkun", "passwordfld:":"xzK343206603","login":"Sign In"}
data = {"__csrf_magic":"sid:6d64fd1547de2c1b0b09fdfd1e8542486d2781c7,1551941284;ip:2580cc5b4a119634e5574130ae0fc9afdc369bec,1551941284","usernamefld":"xiezhenkun","passwordfld":"xzK343206603","login":"Sign IN"}

###  发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在session?L
session.post(login_url, data = data, verify=False)
session.post(arp_url, data = data, verify=False)
###  session包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页?"
#time.sleep(10)
response = session.get(arp_url)

###  打印响应内容
print (response.text)
