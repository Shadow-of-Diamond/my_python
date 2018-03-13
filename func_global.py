#!/usr/bin/python
# Filenam e: func_global.py
def func():
    global x
    #x = 2
    print ('x is', x) #由于此时还未给x赋值，所以先查语句块外的值，否则报错说x未定义，程序无法运行下去。
    x = 2
    print ('Changed local x to', x)
x = 50
func()
print ('Value of x is', x)