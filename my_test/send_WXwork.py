# -*- coding: UTF-8 -*-
import requests,time,sys

def send_WXwork(title,receiver,msg):
    url = 'http://192.168.1.10:8888/Sender_WXwork'
    now = time.strftime('%Y-%m-%d %H:%M:%S\n')
    title = now + 'Alarm from 192.168.20.22  [sender:192.168.1.10]'
    info = {'title':title,'receiver':receiver,'msg':msg}
    r = requests.post(url, data=info)
    print (r.text)

send_WXwork('test-title','xiezhenkun','测试消息')
