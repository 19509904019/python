"""
键盘上输入以下内容并打印输出：
默认（admin，1234）
用户名：username
密码：password
是否记住密码bool类型，is_remember

如果用户名和密码正确并且is_remember是True表示记住密码，则打印已经记住用户xxxd的密码了
否则打印，没有记住密码需要下次继续输入
"""

username = input("请输入用户名：")
password = input("请输入密码：")
is_remember= False

if username == "admin" and password == "1234":
    #判断
    if is_remember:
        print("已经记住用户{0}的密码啦".format(username))
    else:
        print("没有记住密码，需要下次继续输入")
else:
    print("用户名或者密码输入有误，请重新输入！")

