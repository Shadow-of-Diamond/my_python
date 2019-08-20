#!/usr/bin/python
#current's number of threads
import threading
import time

def worker():
    print ("test")
    time.sleep(1)

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()

print ("\ncurrent has %d threads" % (threading.activeCount()-1))