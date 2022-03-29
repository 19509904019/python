'''
Description: 匿名函数
version: 
Author: yujun
Date: 2022-03-26 17:09:51
LastEditors: yujun
LastEditTime: 2022-03-27 15:06:13
'''

'''
匿名函数定义格式：
lambda 参数列表:返回值运算表达式

使用场合：

'''

# def test():
#     print("------1--------")

# def func(a,f):
#     print('-------->',a)
#     f()

# func(6,test)  #函数名相当于传输了地址


# #等价于下面
# def func(a,f):
#     print('-------->',a)
#     f()

# func(6,lambda:print("------1--------"))  #匿名函数作为参数


'''
一个函数的参数是另一个函数:高阶函数
系统的高阶函数:
max、min、sorted

'''
# list = [i for i in range(1,11)]

# result = min(list)
# print(result)


from functools import reduce


list1 = [('lily', 20), ('ayan', 19), ('yujun', 18), ('Bob', 23)]

# 按照key来排序
result = max(list1, key=lambda x: x[1])
print(result)

# 排序
result = sorted(list1, key=lambda x: x[1])
print(result)

result = sorted(list1, key=lambda x: x[1], reverse=True)
print(result)

# 过滤 filter的匿名函数要求返回值必须是bool类型，只有bool类型结果为True的才是符合过滤条件的
result = filter(lambda x: x[1] >= 20, list1)
print(result)
print(list(result))

#map 通过匿名函数指明提取的内容，并对内容进行加工
result = map(lambda x:x[0].upper(),list1)
print(result)
print(list(result))

#reduce
result = reduce(lambda x,y:x+y,[1,2,3,4,5])
print(result)

#zip
reuslt = zip()