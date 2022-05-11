'''
Description: 装饰器
version: 
Author: yujun
Date: 2022-03-25 20:58:49
LastEditors: yujun
LastEditTime: 2022-03-25 22:00:22
'''

'''
装饰器：
遵循开放封闭原则，在不改变原函数的情况下，扩展了函数的功能

定义：
def xxx(func):
    def xxx():
        ...
        func()
        ...
        return yyy
    return xxx

装饰：
@装饰器名  ----->   原函数 = 装饰(原函数)
def 原函数():
    pass

将原函数(被装饰的函数)的地址作为参数传递给装饰器函数
函数体中出现参数时，此时调用的是未被装饰的函数体

主要看return，return后面接的函数就是装饰函数
'''

'''
带参数的装饰器：
如果原函数有参数则装饰器内部函数也要有参数
'''

'''
装饰器修饰有返回值的函数
原函数有返回值，装饰器的内部函数也要有返回值
'''


# 装饰器就是为了给函数添加新的功能，所以第一步就要调用函数
def decorator(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print("预计装修费用是：{}元".format(r))
        print("刷漆")
        print("铺地板")
        print("买家具")
        print("精装修房子")
        return 60000

    return wrapper


@decorator
def house():
    print("我是一个毛坯房...")
    return 50000


price = house()  # house()就是wrapper  wrapper没有返回值所以为None
# print(price)
