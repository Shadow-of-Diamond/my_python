#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests,os,sys,re
import urllib.request
import urllib.parse
import subprocess

temp_file1 = os.getcwd() + '\\temp1.txt'
temp_file2 = os.getcwd() + '\\temp2.txt'
#temp_file1 = 'C:\\Users\\Administrator\\Desktop\\temp1.txt'
#temp_file2 = 'C:\\Users\\Administrator\\Desktop\\temp2.txt'


def whereis_ip(ip):
	write_temp1 = open(temp_file1,'w')
	url = 'http://www.ip138.com/ips138.asp?ip='+ip
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
	'Accept-Language':' zh-CN,zh;q=0.9',
	}
	request = urllib.request.Request(url=url,headers=headers,)
	response = urllib.request.urlopen(request)
	html = response.read().decode('gbk','replace')
	write_temp1.write(html)
	write_temp1.close()
	read_html = open(temp_file1,'r')
	for line in read_html.readlines():
		if "本站数据" in line:
			data = line.replace("<li>","\n").replace("</li>","").replace("</ul></td>","")
			write_temp2 = open(temp_file2,'w')
			write_temp2.write(data)
			write_temp2.close()
			read_temp2 = open(temp_file2,'r')
			print ("================================\n查询的ip："+ip+'\n')
			for l in read_temp2.readlines():
				if "class" not in l:
					print (l)

def get_ip(url):
  cmd = 'ping -n 1 '+url
  stdout,stderr = subprocess.Popen(cmd,shell=True,universal_newlines=True, stdout=subprocess.PIPE).communicate()
  try:
    ip = stdout.split('[')[1].split(']')[0]
    return ip
  except:
    return ('error')

ip=sys.argv[1]
if re.search(r'((1[0-9][0-9]\.)|(2[0-4][0-9]\.)|(25[0-5]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))',ip) != None:
	whereis_ip(ip)
elif re.search("hk|tw|ru|uk|tv|eu|us|top|com|cn|art|net|edu|gov|int|mil|net|org|biz|info|pro|name|museum|coop|aero|xxx|idv|firm",ip.lower()) != None:
	url_ip = get_ip(ip)
	if url_ip != 'error':
		whereis_ip(url_ip)
	else:
		print ('URL解析错误，请检查')
else:
	print ('非法ip')



if os.path.exists(temp_file1) or os.path.exists(temp_file2) == "True":
	for i in temp_file1,temp_file2:
		os.remove(i)



