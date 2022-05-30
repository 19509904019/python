"""
datetime模块：
    time 时间
    date 日期   (data数据)
    datetime 日期时间   now()
    timedelta 时间差  timedelta(days = '',weeks =  ''...)

"""
import datetime
import time

print(datetime.time.hour)  # 对象

# 因为date是类，所以要求创建对象
d = datetime.date(2022, 1, 1)
print(d)
print(time.ctime(time.time()))
print(datetime.date.ctime(d))
print('-' * 50)

# datetime.timedelta
print(datetime.date.today())  # 2022-04-11 年月日
print('-' * 50)

# datetime.datetime.now()  --->  得到当前的日期和时间  年月日  时分秒
time_now = datetime.datetime.now()
print(time_now)

time1 = datetime.timedelta(hours=0.5)
result = time1 + time_now
print(result)
print('-' * 50)

# 缓存  数据redis 作为缓存  redis.set(key,value,时间差)  会话：session


