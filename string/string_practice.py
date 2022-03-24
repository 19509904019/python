'''
Author: yujun
Date: 2022-03-14 13:57:52
LastEditors: yujun
LastEditTime: 2022-03-14 14:23:26
FilePath: \python_learning\string_practice.py
Description: 

'''
'''
https://i0.hdslb.com/bfs/face/37a0f4baf76199fea4607366ce223ae4105709bd.jpg@240w_240h_1c_1s.webp
'''


import random
path = 'https://i0.hdslb.com/bfs/face/37a0f4baf76199fea4607366ce223ae4105709bd.jpg@240w_240h_1c_1s.webp'

# find,index,rfind,rindex
'''
find:从左向右查找，只要遇到一个符合要求的则返回位置；如果没有找到任何符合要求的，则返回-1
rfind: right find   从右往左查找
count:统计指定字符的个数
index与find区别: index也是表示查找，但是如果找不到会报错
'''
# i = path.find('3')
# print(i)
# print(path[i:])

# i = path.rfind(".")
# print(path[i:])

# i = path.count(".")
# print(i)

'''
判断：startswith,endswith,isalpha,isdigit,isalnum,isspace
返回值都是布尔类型的（True,False）
'''
# s = '37a0f4baf76199fea4607366ce223ae4105709bd.jpg@240w_240h_1c_1s.webp'
# result = s.startswith('37')  #判断是否是以xxx开头的
# print(result)

# result = s.endswith(".mp4")  #判断是否是以xxx结尾的
# print(result)


'''
模拟文件上传，键盘输入上传文件的名称，判断文件名是否大于6位以上，扩展名是否是：jpg,gif,png格式
如果不是则提示上传失败，如果名字不满足条件，而扩展名满足条件则随机生成一个6位
数字组成的文件名，打印成功上传xxxx.png
'''
'''第一种：固定文件名长度'''
# # 键盘输入上传文件名称
# file = input("请输入上传文件名称:")
# # print(len(file))

# # 判断文件名扩展名
# if file.endswith( "gif") or file.endswith("png") or file.endswith("jpg"):
#     #寻找文件名
#     i = file.rfind(".")
#     filename = file[:i]  #切片
#     #判断文件名长度
#     if len(filename)>6:
#         print("上传成功！")
#     else:
#         filename = random.randint(100000,999999)
#         print("文件名长度不足，随机生成文件名，成功上传{0}{1}".format(filename,file[i:]))

# else:
#     print("文件格式错误，上传失败！")

'''
模拟文件上传，键盘输入上传文件的名称，判断文件名是否大于6位以上，扩展名是否是：jpg,gif,png格式
如果不是则提示上传失败，如果名字不满足条件，而扩展名满足条件则随机生成一个6位
数字组成的文件名，打印成功上传xxxx.png
'''
'''第二种：随机生成文件名'''

# #键盘输入文件名称
# file = input("请输入所要上传文件的名称：")
# #随机生成的文件名集合
# string = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
# #随机生成文件名的个数
# num = 6

# #判断扩展名
# if file.endswith("jpg") or file.endswith("png") or file.endswith("gif"):
#     i = file.rfind(".")
#     #寻找文件名
#     filename = file[:i]
#     if len(filename)<6:
#         #初始化文件名
#         filename = ''
#         #生成文件名
#         for j in range(num):
#             #随机产生下标
#             index = random.randint(0,len(string)-1)
#             filename += string[index]
#             #打印文件名
#         print("文件名不符合要求，已重新加载，文件{0}{1}上传成功".format(filename,file[i:]))
#     else:
#         print("文件{}{}上传成功".format(filename,file[i:]))

# else:
#     print("文件格式错误，上传失败！")

'''
isalpha():判断字符串是否全是字母
isdigit():判断字符串是否全是数字
istitle():判断首字母是否是大写
islower():判断是否全为小写字母
isupper():判断是否全是大写字母
'''
# string1 = 'helloworld'
# string2 = 'helloworld123'
# string3 = '123456'
# result1 = string1.isalpha()
# print(result1)
# result2 = string2.isalnum()
# print(result2)
# result3 = string3.isdigit()
# print(result3)

'''
admin123   15811119999  202225
用户名或者手机号码登陆+密码
用户名：全部小写，首字母不能是数字，长度必须是6位以上
手机号码：纯数字  长度为11位
密码必须是6位数字

以上符合条件则进入下层验证：
判断用户名和密码是正确的，提示登陆成功
否则登陆失败
'''
flag = True
count = 0
while flag:
    # 判断是否使用用户名登录
    login = input("是否有用户名(y/n，不区分大小写):")
    # 使用用户名登录
    if login.lower() == "y":
        #循环输入用户名
        while flag:
            # 输入用户名
            username = input("请输入用户名：")
            # 判断用户名是否符合格式
            if username.islower() and not username[0].isdigit() and len(username) > 6:
                #循环输入密码
                while True:
                    password = input("请输入用户密码：")
                    # 判断密码是否符合格式
                    if password.isdigit() and len(password) == 6:
                        print("登录成功！")
                        flag = False  #外层循环退出条件
                        break
                    else:
                        print("密码格式输入错误，输入三次将锁定!")
                        count += 1
                        if count == 3:
                            print("密码输入错误三次，已锁定！")
                            flag = False
                            break
            else:
                print("用户名输入错误，请重新输入，五次错误后将自动退出！")
                count += 1
                if count == 5:
                    print("用户名输入错误五次，已退出！")
                    flag = False
                    break

    # 不使用用户名登录
    elif login == "n" or login =="N":
        while flag:
            telnum = input("请输入手机号码：")
            # 判断手机号是否符合格式
            if telnum.isdigit() and len(telnum) == 11:
               while True:
                    password = input("请输入用户密码：")
                    # 判断密码是否符合格式
                    if password.isdigit() and len(password) == 6:
                        print("登录成功！")
                        flag = False
                        break
                    else:
                        print("密码格式输入错误，输入三次将锁定!")
                        count += 1
                        if count == 3:
                            print("密码输入错误三次，已锁定！")
                            flag = False
                            break
            else:
                print("手机号输入错误，请重新输入，五次错误后将自动退出！")
                count += 1
                if count == 5:
                    print("手机号输入错误五次，已退出！")
                    flag = False
                    break
    else:
        print("请输入y/n!")
