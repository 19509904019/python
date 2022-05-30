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

'''
library = [书名1，书名2，...]

def add_book(bookname):
    pass

def all_book(library):
    pass

依次调用
'''


'''
可变参数:
*args
**kwargs

拆包和装包
函数装包：
def 函数(*args):  -----> 此时会出现装包操作
    pass
函数(1,2,3,4)

拆包：
list,tuple,set
调用的时候：
函数(*list) | 函数(*tuple) |  函数(*set)   -----> 拆包

'''
# #求和
def get_sum(*args):
    # print(args)
    sum = ''
    for i in args:
        sum += i
    print(sum)
    

list = ['a','b','c']
get_sum(*list)

'''
可变参数：**kwargs
关键字参数
在函数调用的时候必须传递关键字参数，才可以将其转换成key:value
将其装到字典中
'''
def show_book(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)

dict = {'bookname' :'红楼梦','author': '曹雪芹','price': 88}
show_book(**dict)


'''
可变参数：
*args  **kwargs
arguments 
'''

'''
参数：外界向里面传值
返回值：里面的内容向外界传送

def 函数名(参数，...):
    ...
    ...
    return xxxx

当函数调用时通过return向外返出值
注意：只要函数有返回值，也可以是多个值

return 后面的值可以是一个值，也可以是多个值
如果是多个值 类似：return a,b,c  会将多个值封装到一个元组中
将元组作为整体返回
结果：(a,b,c)
'''
def get_num(*args):
    total = 0
    for i in args:
        total += i
    return total
list = [i for i in range(1,101)]
# print(list)
total = get_num(*list)
print(total)

'''
全局和局部变量：
声明函数外面的称作全局变量
声明函数内部的变量称作局部变量

函数内部可以直接使用全局变量，但是不能直接修改全局变量
如果想修改全局变量，则必须必须使用关键字：global 全局变量名
'''

'''
全局和局部变量：
global关键字的添加：
只有不可变的类型才需要添加global
可变的类型不需要添加global


可变与不可变：
不可变：当改变变量的值时，地址发生了改变
        类型：int str float bool tuple （不可以增删改）
可变：当改变变量的值时，地址没发生改变
        类型：list,dict,set （可以增删改）
'''

'''
return:
return 返回多个参数时自动返回为元组形式
后面也可以接字符串、列表、字典等形式
如：return ['a','b']

返回字典的时候默认返回字典的键
'''


'''
引用：
1.不是函数中使用，可以通过sys.getrefcount(a) 查看引用个数
    del 变量  表示删除了一个引用

2.函数定义后，在调用函数时：
当实参的地址不发生变化时相当于传递了实参的地址，此时形参改变也会改变实参
list、dict、string
当实参的地址发生变化时相当于传递的是值，此时形参改变不影响实参的变化
int、float、tuple...
'''
