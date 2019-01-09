#!/usr/bin/python
# Filenam e: func_key.py
def func(a, b=5, c=10):
    print ('a is',a,'and b is',b,'and c is',c)
func(3, 7)
func(1,2,3)
func(25, c=24)
func(c=50, a=100)
func(b=2,a=1)

#形参的指定：建议要么全部用abc指定，要么按照顺序指定