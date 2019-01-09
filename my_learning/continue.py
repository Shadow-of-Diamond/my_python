#!/usr/bin/python
# Filenam e: continue.py
while True:
    s=input('Enter something : ')
    #print(len(s))
    if s == 'quit':
        break
    elif len(s) < 3:
        #print(len(s))
        continue
    print ('Input is of sufficient length')
# Do other kinds of processing here...