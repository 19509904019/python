'''
Description: 文件操作
version: 
Author: yujun
Date: 2022-03-26 21:28:47
LastEditors: yujun
LastEditTime: 2022-03-27 11:12:27
'''

'''
文件上传：
保存log

系统函数：
open(file,mode,buffering,encoding)

mode: r  w  rb   wb

r, w: 纯文本文件
rb,wb:纯文本  图片  音乐  视频

r:输入
w:输出

缓存：buffering  调节硬件和CPU之间的缓冲
编码：encoding
'''
'''
读：
    open(path/filename,'rt')  -----> 返回值：stream(管道)
    stream.read()  -----> 读取管道中的内容
注意：如果传递的path/filename有误，则会报错：FileNotFoundError
      如果是图片则不能使用默认的读取方式，mode = 'rb'

总结：
    read() : 读取文件
    readline() : 每次读取一行内容
    readlines(): 读取所有的行保存到列表中
    readable() : 判断是否可读
'''
stream = open(r'C:\Users\12414\Desktop\score.txt',encoding='UTF-8')  #当成是一个管道，暂存文件的内容
# container = stream.read()
# print(container) 


result = stream.readable()  #判断文件是否可读 True False
print(result)

# while True:
#     result = stream.readline()  #按行来输出
#     print(result)
#     if not result:
#         break

result = stream.readlines()
for i in result:
    print(i)