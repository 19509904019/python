"""
time 模块
1.时间戳

"""
import time

# 起始时间
t = time.time()
# 终止时间
t1 = time.time()
# 时间差
t2 = t1 - t
print(t)
# print(t2)
print('-' * 50)

# 将时间转换成字符串
s = time.ctime(t)
print(s)
print('-' * 50)

# 将时间戳转成元组
t3 = time.localtime(t)
print(t3)
print(t3.tm_hour)
print(t3.tm_yday)
print('-' * 50)

# 将元组转成时间戳
tt = time.mktime(t3)
print(tt)
print('-' * 50)

# 将元组转成字符串
s = time.strftime('%Y-%m-%d %H:%M:%S')
print(s)
print('-' * 50)

# 将字符串转成元组的方式
r = time.strptime('2022-04-12', '%Y/%m/%d \n')
print(r)

'''
time模块：
重点：
    time()
    sleep()
    strftime('格式') 
    
了解：
    元组  ----> t.tm_mon  t.tm_wday...
    
'''
