'''
图书管理:
借书 ----->  查询 书
还书 ----->  查询 书
公用查询功能

函数：复用
格式：
def 函数名([参数, ....]):
    代码

函数名:get_name()
       search()
代码：
    封装重复内容

调用：函数名()
'''
# 生成验证码
import random
def generate_code():
    # 验证码字符
    strings = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # 保存验证码
    code = ''
    # 生成四位数验证码
    for i in range(4):
        # index = random.randint(0,len(strings)-1)
        # code += strings[index]
        code += random.choice(strings)
    print(code)


# print(type(generate_code))
# 验证函数是否可用:调用函数，开始执行函数中的代码
# generate_code()


'''
参数：
1.无参数
2.有参数

无参数：
def 函数名():
    pass

有参数：
def 函数名(参数1，参数2，参数3，...):
    pass
'''
def generate_code(n):
    # 验证码字符
    strings = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # 保存验证码
    code = ''
    # 生成四位数验证码
    for i in range(n):
        code += random.choice(strings)
    print(code)

# number = int(input("输入生成位数:"))
generate_code(4)

'''
带多个参数的函数

def 函数名(参数1，参数2):
    函数体
'''
def get_sum(a,b):
    c = a+b
    print(c)
get_sum(2,3)

'''
默认值参数：在定义函数的时候，有一个或者多个参数已经赋值
def 函数名(参数1，参数2，参数3 = 值，参数4 = 值，...):
    函数体

调用特点：
函数名(值1，值2)

注意：
1.在定义函数的时候，普通参数要位于默认值参数的前面
2.默认参数的顺序是固定的，调用时使用关键字参数传值
'''

