#!/usr/bin/python
# Filename: lambda.py
def make_repeater(n):
    return lambda s:s+n
twice = make_repeater(2)
#print (twice('test1'))
print (twice(5))

g = lambda x, y, z : (x + y) ** z
print (g(1,2,3))

'''
lambda与def函数功能类似，但也有区别：
1）def创建的方法是有名称的，而lambda没有。 
2）lambda会返回一个函数对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）。 
3）lambda只是一个表达式，而def则是一个语句。 
4）lambda表达式” : “后面，只能有一个表达式，def则可以有多个。 
5）像if或for或print等语句不能用于lambda中，def可以。 
6）lambda一般用来定义简单的函数，而def可以定义复杂的函数。 
6）lambda函数不能共享给别的程序调用，def可以。 
'''