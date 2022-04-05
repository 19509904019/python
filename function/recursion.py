'''
Description: 递归函数
version: 
Author: yujun
Date: 2022-03-26 16:20:12
LastEditors: yujun
LastEditTime: 2022-03-26 17:29:49
'''

'''
如果一个函数在内部不调用其他函数，而是自己本身的话，这个函数就是递归函数
遵循：
1.必须要有出口
2.每次递归向出口靠近
'''


# #打印1-10
# def print_number(count):
#     count += 1
#     print(count)
#     if count == 10:
#         return
#     print_number(count)

# print_number(0)

# 求递归最好依次递减
# 1-10累加和
# sum = 0
# def get_sum(n,m): #n为起始值，m为终止值
#     global sum
#     sum += n
#     n += 1
#     if n == m+1:
#         print("累加和为{}".format(sum))
#         return

#     get_sum(n,m)

# get_sum(1,10)

# def get_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + get_sum(n - 1)

# sum = get_sum(100)
# print(sum)

# #阶乘
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# sum = factorial(5)
# print(sum)

# 斐波那契数列 1、1、2、3、5、8、13...


# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1)+fibonacci(n-2)

# list = [fibonacci(i) for i in range(1,11)]
# print(list)

# 不用递归用循环
def fib_loop_for(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(1, 10):
    print(fib_loop_for(i), end=" ")


