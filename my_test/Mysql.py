#!/usr/bin/python
# -*- coding: UTF-8 -*-
#测试连接数据库

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



inser_user_list = []
remove_user_list = []
passwd_user_list = []
renew_user_list = []
reply_post_list = []
reset_passwd_list = []


host = '192.168.1.229'
db_username = 'xiezhenkun'
db_password = 'xzK343206603'
db_name = 'radius'

db = pymysql.connect(host=host, user=db_username, password=db_password, db=db_name)
cursor = db.cursor()
sql = "select host,user from mysql.user;"
cursor.execute(sql)
results = cursor.fetchall()
print (results)
db.close()