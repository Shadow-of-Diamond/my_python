#coding:utf-8
### 中文转拼音

from xpinyin import  Pinyin
import sys

def pinyin(name):
    p = Pinyin()
    output = p.get_pinyin(name,'')
    print (output)
#    return (output)


#name = sys.argv[1]
name = '测试'
pinyin(name)