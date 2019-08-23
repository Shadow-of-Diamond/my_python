#coding:UTF-8
import requests
import re

login_url = 'http://192.168.1.209:8888/admin/login.pl'
arp_url = 'http://192.168.1.209:8888/admin/info_arpcache.pl'
keywords = 'class|align|href'
ip_list = []
mac_list = []
arp_list = []

def hsroute():
    session = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    data = {"loginid": "xiezhenkun","passwd": "29ab20c716a35cb80722617ee355227c", "save": "on", "ok": "登录"}
    session.post(login_url, data=data)
    response = session.get(arp_url)
    keywords = 'class|align|href'
    data = response.text
    for line in data.split('\n'):
        if re.search(keywords, line) == None and len(line.split('<td>')) == 2 and re.search('</td>', line) != None and re.search('<td>\w+<\/td>', line) == None:
            newline = line.split('<td>')[1].split('</td>')[0].replace('&nbsp;', '').strip()
            #print (newline)
            if re.search('-', newline) == None:
                ip_list.append(newline)
            else:
                mac_list.append(newline)
    if len(ip_list) == len(mac_list):
        for i in range(len(ip_list)):
            arp_list.append(ip_list[i] + '\t\t' + mac_list[i])
            print(arp_list)

hsroute()



