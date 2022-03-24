# '''
# 定义一个login函数：
# admin 1234
# 输入用户名和密码，验证是否正确
# '''
# def login():
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == 'admin' and password == '1234':
#         print("登录成功！")
#     else:
#         print("输入错误，请重新输入！")
# login()


# # 带参数，n表示允许输入错误的次数
# def login(n):
#     # 登录次数
#     count = 0
#     while True:
#         username = input("请输入用户名:")
#         password = input("请输入密码:")
#         # 登录条件
#         if username == 'admin' and password == '1234':
#             print("登录成功！")
#             break
#         else:
#             print(f"登录失败,失败{n}次会锁定！")
#             count += 1
#         # 错误次数
#         if count == n:
#             print(f"输入{n}次，已锁定！")
#             break
# # 调用函数
# login(3)


# # 求1-n的累加和
# def get_sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     print(sum)


# get_sum(100)


'''
(多个参数)
定义一个出租车打车程序，参数：手机号码，起步价：10元
函数体中输入乘车时间和里程数，2公里内起步价
超出2公里每公里5元，乘车时间每分钟0.5元
下车打印总账单
'''


