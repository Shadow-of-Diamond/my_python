import requests,time,sys,datetime,subprocess

def get_ip(url):
    cmd = 'ping -n 1 '+url
    stdout,stderr = subprocess.Popen(cmd,shell=True,universal_newlines=True, stdout=subprocess.PIPE).communicate()
    try:
        ip = stdout.split('[')[1].split(']')[0]
        return ip
    except:
        return ('error')


def get_code(web):
    time_now = datetime.datetime.now()
    now = time_now.strftime('%Y.%m.%d-%H:%M:%S')
    url = web.split('//')[1]
    ip = get_ip(url)
    if ip == 'error':
        msg = web+'域名无法解析出IP，请检查'
        print (msg)
    else:
        try:
            web_code=requests.get(web,timeout=5).status_code
            msg = url + "\'s web code is " + str(web_code) + ' -- ' + ip + '\t' + now
            print (msg)
        except Exception as e:
            print (url + ' is timeout - 5s')
            pass

def check(web): #定义一个死循环去不停地检测
    i = 1
    while i > 0:
        i = i + 1
        get_code(web)
        time.sleep(1)

web = 'https://' + sys.argv[1]
#web = 'http://www.pcauto.com.cn'
check(web)