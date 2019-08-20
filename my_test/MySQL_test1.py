#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import datetime
import logging
import logging.handlers
import random
import string
import time
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import json

order_list = [{"created_time":"2001-10-12 10:02:58","expiration":"2018-02-10","mail":"xiezhenkun@pconline.com.cn","oper_type":"custom","order_no":"NETWORK-2001-61","username":"xiezhenkun"},{"created_time":"2018-05-15 15:35:15","expiration":"2018-10-29","mail":"gaozhenping@pcauto.com.cn","oper_type":"remove","order_no":"NETWORK-2018-1883","username":"gaozhenping"}]

inser_user_list = []
remove_user_list = []
passwd_user_list = []
renew_user_list = []
reply_post_list = []
reset_passwd_list = []

for i in order_list:
    if i['oper_type'] == 'add':         #新增用户
        inser_user_list.append(i)
    elif i['oper_type'] == 'remove':    #删除用户
        remove_user_list.append(i)
    elif i['oper_type'] == 'passwd':    #修改用户密码（重新生成随机密码）
        passwd_user_list.append(i)
    elif i['oper_type'] == 'renew':     #账号续期
        renew_user_list.append(i)
    elif i['oper_type'] == 'custom':
        reset_passwd_list.append(i)

#print (reset_passwd_list)
#print (remove_user_list)

if reset_passwd_list != []:
   for i in reset_passwd_list:
        order_no = i["order_no"]
        username = i["username"]
        print (username)




















