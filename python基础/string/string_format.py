'''
格式化：
1. %d %s %f.....
    print('一个 %s'%xxxx)
2.format

'''
# #不使用数字填充
# name = '阿燕'
# age = 18
# print("{}今年{}岁".format(name,age))


# #使用数字填充，从0开始计数
# name = '阿燕'
# age = 18
# print("{0}今年{1}岁,我也{1}岁".format(name,age))

# #变量名的形式，format的参数必须是关键字参数
# result = "{name}今年{age}岁,我也{age}岁".format(name='阿燕',age=18)
# print(result)


'''
模拟论坛：
1.输入所提的问题
2.输入用户名
3.回复：
回复的内容不能为空，不能含有敏感词汇，最多评论20个字（显示剩余多少字）
回复的内容前后不能有空格
'''

flag = True

while flag:
    # 注册用户名
    username = input("请注册用户名：")
    # 用户名判断
    if username.islower() and not username[0].isdigit():
        username = username.strip()  # 自动删除空格
        # print(len(username))
        while flag:
            # 输入注册密码
            password = input("请输入注册密码：")
            password = password.strip()
            # 密码判断
            if not password.isdigit() and len(password) >= 8:
                print("注册成功！")
                flag = False
            else:
                print("密码格式错误，密码不能仅含数字，长度不能少于8位！")
    else:
        print("用户名格式错误,字母为小写且不能含有空格，开头不能为数字！")

# print(username,password)
# 分割符号
print('-'*50)

flag = True
count = 0
# 用户登录
while flag:
    username_login = input("请输入用户名：")
    password_login = input("请输入登录密码：")
    if username_login == username and password_login == password:
        print("登录成功！")
        flag = False
    else:
        print("登录失败，用户名或密码错误，请重新登录！")

print('-'*50)
# 输入问题
while True:
    question = input("问题：\n")
    # 输入的问题不能为空
    if len(question.strip()) != 0:
        # 敏感词汇替换
        question = question.replace('滚蛋', '**')
        print("输入的问题为：%s" % question)
        break
    else:
        print("输入的问题不能为空，请重新输入！")

print('-'*50)
print("评论\n")
# 输入问题答案
while True:
    answer = input("输入内容:\n")
    # 验证内容是否符合要求 不能为空  长度不超过20  敏感词汇
    if not answer.isspace() and len(answer) <= 20:
        answer = answer.replace('蠢货', '**')
        print("{}的评论为：{}".format(username, answer))
    else:
        print("评论内容不能为空,请重新输入！")
