#python3
#计算定义日期为当前的前多少天

import datetime

expire_days = '10'
now_day = datetime.datetime.today()
#theday = now - datetime.timedelta(days=int(expire_days))

getday = '2019-08-20'

getday_year = int(getday.split('-')[0])
getday_mon = int(getday.split('-')[1])
getday_day = int(getday.split('-')[2])

theday = datetime.datetime(getday_year,getday_mon,getday_day)
#print (now_day)
print ((now_day - theday).days)