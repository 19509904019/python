"""
最多输入用户名和密码三次，如果三次都没有登录成功则提示用户账号被锁定

"""
count = 0
for i in range(3):
    # 提示输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 判断用户名和密码是否正确 admin 123
    if username == "admin" and password == "123":
        print("用户登录成功！")
        break
    else:
        print("用户名或密码输入错误，请重新输入...")

    count += 1
    # 账号锁定判断
    if count == 3:
        print("三次输入错误，账号已经被锁定！")
