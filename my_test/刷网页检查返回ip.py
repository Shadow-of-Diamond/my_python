#coding:utf-8
import urllib2,os,logging.handlers
import Utils.send

LOG_FILENAME = os.getcwd() + '/log.txt'
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5120 * 5120, backupCount=10)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('tst') 
logger.addHandler(handler)

###刷取网页检查返回ip是否正确
url = 'http://adtool.pc.com.cn/headers/'
my_ip = '192.168.1.10'
data = urllib2.urlopen(url).read()
req_ip = data.split('\n')[3].split(':')[1].split(',')[0]

def check():
    if req_ip == my_ip:
        print ('my_ip is ' + my_ip)
        print ('req_ip is ' + req_ip + '\n')
    else:
        print ('my_ip != req_ip,please check')
        logger.info(data)

for i in range(0,10):
    check()
