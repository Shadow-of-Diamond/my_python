#!/usr/bin/python
# Filenam e: func_local.py
def func(x):
    #x = 2
    print ('x is', x) #由于此时还未给x赋值，所以先查语句块外的值，否则报错说x未定义，程序无法运行下去。
    x = 2 #局部变量
    print ('Changed local x to', x)
x = 50
func(x)
print ('x is still', x)