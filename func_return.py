#!/usr/bin/python
# Filenam e: func_return.py
def maximum (x, y):
    if x > y:
        return x
    elif x == y:
        a=x+y
        print(a)
        return x #执行return后，直接退出语句块。
        #print (a)  #如执行上行return，此句不会执行
    else:
        return y
print (maximum (4, 4))