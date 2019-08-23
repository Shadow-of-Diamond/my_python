#coding:utf-8
import urllib.request as urllib
import os,logging.handlers,sys,re
#import Utils.send
#检查网页返回ip

#LOG_FILENAME = sys.path[0] + '/log.txt'
#handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5120 * 5120, backupCount=10)
#fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
#formatter = logging.Formatter(fmt)
#handler.setFormatter(formatter)
#logger = logging.getLogger('tst') 
#logger.addHandler(handler)

###刷取网页检查返回ip是否正确
url = 'http://adtool.pc.com.cn/headers/'
my_ip = '192.168.1.10'
url_data = urllib.urlopen(url).read()
data = url_data.decode(encoding='utf-8')
req_ip = data.split('\n')[3].split(':')[1].split(',')[0]
     
print (req_ip)

#def check():
#    if req_ip == my_ip:
#        print ('my_ip is ' + my_ip)
#        print ('req_ip is ' + req_ip + '\n')
#    else:
#        print ('my_ip != req_ip,please check')
#        logger.info(data)
#
#for i in range(0,10):
#    check()
