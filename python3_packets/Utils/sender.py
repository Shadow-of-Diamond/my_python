# -*- coding: UTF-8 -*-
import requests,time,sys,json

def WXwork(title,receiver,msg):
    url = 'http://192.168.1.10:8888/Sender_WXwork'
    now = time.strftime('%Y-%m-%d %H:%M:%S\n')
    title = now + 'Alarm from 192.168.1.46  [sender:192.168.1.10]'
    info = {'title':title,'receiver':receiver,'msg':msg}
    r = requests.post(url, data=info)
    print (r.text)


def wx(receiver,msg):
    url = 'http://192.168.1.10:8888/Sender_wx'
    now = time.strftime('%Y-%m-%d %H:%M:%S\n')
    title = now + 'Alarm from 192.168.1.46  [sender:192.168.1.10]'
    info = {'receiver':receiver,'msg':msg}
    r = requests.post(url, data=info)
    print (r.text)


def mail(title,receiver,msg):
    url = 'http://192.168.1.10:8888/Sender_mail'
#    now = time.strftime('%Y-%m-%d %H:%M:%S\n')
#    title = now + 'Alarm from 192.168.162.11  [sender:192.168.1.10]'
    info = {'title':title,'receiver':receiver,'msg':msg}
    r = requests.post(url, data=info)
    print (r.text)







#mail_receiver = ['xiezhenkun@pconline.com.cn']
#mail("test-title",json.dumps(mail_receiver),"test-msg")
