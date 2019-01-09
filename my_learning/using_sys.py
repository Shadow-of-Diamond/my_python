#!/usr/bin/python
# Filenam e: using_sys.py
import sys
#print(sys.argv[0])
print ('The command line arguments are:')
for i in sys.argv:
    print (i)
    #pass
print ('\n\nThe PYTHON PATH is', sys.path, '\n')