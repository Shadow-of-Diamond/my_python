#!/usr/bin/python
# Filenam e: func_default.py
def say(message, times = 5): #默认赋值的形参只能放在括号最后位置
    print (message * times)
say('Hello') #默认情况下输出次数为5
say('World', 2)  #如果定义了次数，则按照定义的去输出