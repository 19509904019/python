'''
Description: 闭包
version: 
Author: yujun
Date: 2022-03-25 16:37:26
LastEditors: yujun
LastEditTime: 2022-03-25 17:20:05
'''

'''
嵌套函数
'''


def outer():
    a = 100

    def inner():
        b = 200
        # b += a  #内部函数可以使用外部函数的变量
        nonlocal a  # 如果想修改外部函数的变量，需要在内部函数中添加：nonlocal
        a += b
        print("我是内部函数", a, b)

    print(a)
    inner()


outer()


'''
闭包：
1.嵌套函数
2.内部函数引用了外部函数的变量
3.返回值是内部函数
outer(5)()

r = out(5)
r()

即在一个内部函数里，对外部作用域的变量进行引用，那么内部函数就被认为是闭包
'''


def outer(n):
    a = 200

    def inner():
        b = n + a
        print("内部函数:", b)

    return inner

outer(5)()

