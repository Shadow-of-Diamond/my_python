#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, os, re, hashlib, subprocess ,urllib.request


def get_md5_01(file_path1):
    md5 = None
    if os.path.isfile(file_path1):
        f = open(file_path1, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


if __name__ == "__main__":
    file_path1 = r'e:\dnslist.txt'
    mymd5 = get_md5_01(file_path1)
    print (mymd5)

# os.system("echo '"+md5_01+"' > /data/dnslist_cname/mymd5.txt")

url = "http://192.168.1.10/dnslist_cname.txt"
data = urllib.request.urlopen(url).read()
print (data)

#def get_md5_02(file_path2):
#    md5 = None
    #    if os.path.isfile(file_path2):
    #    f = open(file_path2, 'rb')
    #    md5_obj = hashlib.md5()
    #    md5_obj.update(f.read())
    #    hash_code = md5_obj.hexdigest()
    #    f.close()
    #    md5 = str(hash_code).lower()
#    return md5


#if __name__ == "__main__":
#    file_path2 = urllib.request.urlopen('http://192.168.1.10/dnslist_cname.txt').read()
#    hismd5 = get_md5_01(file_path2)
#    print (hismd5)