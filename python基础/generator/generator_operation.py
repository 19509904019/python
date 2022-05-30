"""
通过列表生成式（列表推导式），我们可以直接创建一个列表
但是，受内存限制，列表容量肯定是有限的
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list,从而节省大量的空间。在python中，这种一边循环一边计算的机制，称为生成器：generator

得到生成器的方式：
1.通过列表推导式得到生成器 : 用小括号 ()
"""

# 1
# newlist = [x * 3 for x in range(20)]
# print(newlist)
#
# # 得到生成器
# g = (x * 3 for x in range(20))  # 不是元组推导式
# print(type(g))  # <class 'generator'>

# 方式1：通过__next__()方式得到元素
# print(g.__next__())
# print(g.__next__())

# 方式2：next(生成器对象)  builtins系统内置函数
# print(next(g))
# print(next(g))
# print(next(g))
# try:
#     for i in range(30):  # StopIteration
#         print(next(g))
# except Exception as e:
#     print("没有更多元素了！")

'''
只要函数中出现了yield关键字，说明函数就不是函数了，变成生成器了
'''
# 斐波那契数列
'''
步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4.借助于next(),__next()__得到元素  next(g)   g.__next__()
next()是系统的函数
__next__()是生成器的方法
'''

#
# def fibonacci(length):
#     a, b = 0, 1
#     for i in range(length):
#         a, b = b, a + b
#         yield a
# return '没有更多元素'  # return就是得到的错误提示信息
#
#
# x = fibonacci(10)  # <class 'generator'>
# print(list(x))
# try:
#     for i in range(20):
#         print(next(x), end=' ')
# except Exception as e:
#     print()
#     print(e)


'''
生成器方法：
    __next()__:获取下一个元素
    send(value):向每次生成器调用中传值  注意：第一次调用send(None)
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i  # 暂停和扔出值
        print(i)
        print("temp:", temp)
        i += 1

    return '没有更多的数据'


g = gen()
# print(type(g))
g.send(None)
n1 = g.send("哈哈")  # 生成器会提供一个接口来传值，但原本的赋值不变
print("n1:", n1)
n2 = g.send("嘻嘻")
print("n2:", n2)

'''
进程 > 线程 > 协程

协程交替进行，可以用到生成器
比如同时下载三个视频，每个视频交替下载
'''

# # 搬一块砖听一首歌
# def task1(n):
#     for i in range(n):
#         print("正在搬第{}块砖...".format(i + 1))
#         yield None
#
#
# def task2(n):
#     for i in range(n):
#         print("正在听第{}首歌...".format(i + 1))
#         yield None
#
#
# g1 = task1(5)
# g2 = task2(5)
#
# while True:
#     try:
#         next(g1)
#         next(g2)
#     except:
#         break
