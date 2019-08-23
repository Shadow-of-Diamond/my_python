import datetime

time = datetime.datetime.now()
nowtime = time.strftime('%Y.%m.%d-%H:%M:%S')
hour = time.strftime('%H')

if 3 >= 24-int(hour) >= 0 or 23 >= 24-int(hour) >=16:
    print ('now is night-time')
else:
    print ('now is work-time')
#print (hour)