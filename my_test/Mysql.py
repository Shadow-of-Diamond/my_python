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

order_list = [{"created_time":"2001-10-12 10:02:58","expiration":"2018-02-10","mail":"xiezhenkun@pconline.com.cn","oper_type":"add","order_no":"NETWORK-2001-61","username":"xiezhenkun"}]

#print (order_list)

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

host = '192.168.13.1'
db_username = 'xiezhenkun'
db_password = '343206603'
db_name = 'radius'

db = pymysql.connect(host=host, user=db_username, password=db_password, db=db_name)
cursor = db.cursor()
sql = "select host,user from mysql.user;"
cursor.execute(sql)
results = cursor.fetchall()
print (results)
db.close()