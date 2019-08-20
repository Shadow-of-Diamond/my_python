import re,sys,os
import urllib.request as urllib

log = "C:\\Users\\Administrator\\Desktop\\1.txt"
url = 'http://192.168.1.10/dnslist_cname.txt'

url_read = urllib.urlopen(url)
data = str(url_read.read()).replace('\\n','\n').replace('b\'','').replace('\"','')

log_w = open(log,'w')
log_w.write(data)
log_w.close()

log_r = open(log,'r')

for line in log_r.readlines():
	domain = line.split()[0]
#	print (domain)
	if re.search(r'.*pc.*\.com\.cn$',domain):
#		print (line)
		pass
	else:
#		pass
		print (line)

log_r.close()
os.remove(log)