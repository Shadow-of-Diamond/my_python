# -*- coding: UTF-8 -*-
import csv


sql_list = []
file = csv.reader(open('E:\\my_python\\my_learning\\src\\vip.csv','r'))
for i in file:
    sql_list.append(i)

print (sql_list)