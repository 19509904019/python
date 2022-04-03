"""
Description: 文件操作
Author: yujun
Date: 2022-03-26 21:28:47
LastEditors: yujun
"""

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

# 复制文件到当前路径下
# with open(r'C:\Users\12414\Desktop\yan.jpg', 'rb') as stream:
#     container = stream.read()  # 读取文件内容

#     path = os.path.dirname(__file__)  # 本地文件路径
#     file_path = stream.name
#     # filename = file_path[file_path.rfind('\\')+1:]  # 文件名称
#     filename_split = os.path.split(file_path)
#     filename = filename_split[1]
#     path1 = os.path.join(path, filename)  # 对地址进行拼接

#     with open(path1,'wb') as wstream:
#         wstream.write(container)

# with open(r'D:\python_learning\file\yan.jpg','rb') as stream:
#     container = stream.read()
#     path = os.path.dirname(__file__)  #文件所在路径
#     filename = os.path.split(stream.name)[1]  #文件名称
#     path1 = os.path.join(path,filename)  #路径拼接
#     # print(path1)
#     with open(path1,'wb') as wstream:
#         wstream.write(container)

'''
os.path

dirname() 获取当前文件所在的文件夹
join()  拼接
split()   文件名称
splitext()  后缀名
getsize()  文件大小

isabs()
isfile()  
isdir()

'''
# path = r'D:\python_learning\file\yan.jpg'

# result = os.path.split(path)[1]  #分割文件名与路径
# print(result)    

# result = os.path.splitext(path)[1]  #分割文件与扩展名
# print(result)

# result = os.path.getsize(path)  #获取文件的大小  单位字节
# print(result)


# result = os.path.join(os.getcwd(),'123.abc')
# print(result)


'''
os.path 里面的函数
os中的函数：
os.getcwd()  # 获取当前目录
os.listdir()  # 浏览文件夹
os.mkdir()  # 创建文件夹
os.rmdir()  # 删除一个空文件夹
os.removedirs() # 删除到不为空的文件夹，当最后一个文件夹不为空时则报错
os.remove()  # 删除文件
os.chdir()  # 切换目录

'''


# dir = os.getcwd()
# print(dir)

# all = os.listdir(r'C:\Users\Dell\Desktop\p1')  # 返回指定目录下的所有文件和文件夹，保存到列表中
# print(all)

# 创建文件夹
# os.mkdir(r'C:\Users\Dell\Desktop\p2')
# if not os.path.exists(r'C:\Users\Dell\Desktop\p2'):
#     os.mkdir(r'C:\Users\Dell\Desktop\p2')

# 删除文件夹
# os.rmdir(r'C:\Users\Dell\Desktop\p2')   # 只删除空的文件夹

# os.removedirs(r'C:\Users\Dell\Desktop\p1\p2')  # 最后一个子目录

# 删除文件
# os.remove(r'C:\Users\Dell\Desktop\p1\p2')  # 只能删除文件

# path = r'C:\Users\Dell\Desktop\p1\p2'
# filelist = os.listdir(path)  # ['123.txt']
# print(filelist)
# for file in filelist:
#     # 删除文件
#     path1 = os.path.join(path, file)
#     os.remove(path1)
# else:
#     # 删除文件所在的文件夹
#     os.rmdir(path)
#     os.rmdir(path[:path.rfind('\\')])

# 切换目录  相当于cd : change direction
# os.chdir(r'C:\Users\Dell\Desktop\深度学习')
# path = os.getcwd()
# print(path)


'''
文件复制

'''
src_path = r'C:\Users\Dell\Desktop\p1'
target_path = r'C:\Users\Dell\Desktop\p2'

# 封装成函数
'''没有文件夹的情况下'''
# def copy(src, target):
#     if os.path.isdir(src) and os.path.isdir(target):
#         # 文件夹里面的所有文件名
#         filename = os.listdir(src)
#         # 遍历所有文件
#         for file in filename:
#             path1 = os.path.join(src, file)  # 文件的绝对路径
#             # 读文件
#             with open(path1, 'rb') as rstream:
#                 container = rstream.read()
#                 # 写文件
#                 path2 = os.path.join(target, file)
#                 with open(path2, 'wb') as wstream:
#                     wstream.write(container)
#         print("复制成功!")
#
#
# # 调用函数
# copy(src_path, target_path)


'''文件中还有文件夹'''


def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        # 打开原文件夹
        filename = os.listdir(src)
        # 读取文件夹内容
        for file in filename:
            # 拼接文件路径
            src_file = os.path.join(src, file)
            # 判断是否为新文件夹
            if os.path.isdir(src_file):
                # 复制文件夹
                target_file = os.path.join(target, file)
                os.mkdir(target_file)
                copy(src_file, target_file)
            else:
                # 读取文件内容
                with open(src_file, 'rb') as rstream:
                    container = rstream.read()
                    # 复制文件内容
                    with open(os.path.join(target, file), 'wb') as wstream:
                        wstream.write(container)


# 调用函数
copy(src_path, target_path)
print("复制成功！")
