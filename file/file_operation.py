'''
Author: yujun
Date: 2022-03-27 14:10:45
LastEditors: yujun
LastEditTime: 2022-03-27 14:59:55
FilePath: \python_learning\file\file_operation.py
Description: 
'''
'''
Description: 文件操作
version: 
Author: yujun
Date: 2022-03-26 21:28:47
LastEditors: yujun
LastEditTime: 2022-03-27 14:08:46
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
# stream = open(r'C:\Users\12414\Desktop\score.txt','r',encoding='UTF-8')  #当成是一个管道，暂存文件的内容
# # container = stream.read()
# # print(container)


# result = stream.readable()  #判断文件是否可读 True False
# print(result)

# # while True:
# #     result = stream.readline()  #按行来输出
# #     print(result)
# #     if not result:
# #         break

# result = stream.readlines()
# for i in result:
#     print(i)


'''
w ：写文件，即修改文件,每次都会将内容清空
write(写内容)  每次都会将原来的内容清空，然后写当前的内容
writelines(Iterable)  没有换行效果
stream.writelines(['字符1 \n','字符2 \n','字符3 \n','字符4 \n','字符5 \n'...])


如果mode = 'a'
则只会追加不会清空
'''

# stream = open(r'C:\Users\12414\Desktop\score.txt','w',encoding='UTF-8')

# # result = stream.writable()
# # print(result)

# # string = '今天是2022 - 3 - 27 \n又是学习的一天'
# # result = stream.write(string)
# # print(result)
# # stream.close()

# # a 模式  即append
# stream = open(r'C:\Users\12414\Desktop\score.txt','a',encoding='UTF-8')

# # result = stream.writable()
# # print(result)

# string = '今天是2022 - 3 - 27 \n又是学习的一天'
# result = stream.write(string)
# print(result)
# stream.close()


'''
文件的复制：

原文件：C:\\Users\\12414\\Desktop\\yan.jpg
目标文件：C:\\Users\\12414\\Desktop\\yan.jpg

with结合open使用，可以帮助我们自动释放资源
即最后不用close()
'''

# with open(r'C:\Users\12414\Desktop\yan.jpg','rb') as stream:
#     container = stream.read()  #读取文件内容

#     with open(r'E:\p1\yan.jpg','wb') as wstream:
#         wstream.write(container)

# print("复制完成！")

'''
模块：xxx.py
os.py


os.path:
path = os.path.dirname(__file__) 获取当前文件所在的文件目录（绝对路径）
path1 = os.path.join(path,'命名文件名')  返回的是一个拼接后的新的路径
'''

import os
with open(r'C:\Users\12414\Desktop\yan.jpg', 'rb') as stream:
    container = stream.read()  # 读取文件内容

    path = os.path.dirname(__file__)  # 本地文件路径
    file_path = stream.name
    # filename = file_path[file_path.rfind('\\')+1:]  # 文件名称
    filename_split = os.path.split(file_path)
    filename = filename_split[1]
    path1 = os.path.join(path, filename)  # 对地址进行拼接

    with open(path1,'wb') as wstream:
        wstream.write(container)

