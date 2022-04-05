"""
可迭代的对象：1.生成器  2.元组  列表  集合   字典   字符串

如何判断一个对象是否可迭代？
isinstance(判断对象,Iterable)
"""
from collections.abc import Iterable

list1 = [1, 3, 6, 8, 4]
f = isinstance(list1, Iterable)
print(f)

f = isinstance(100, Iterable)
print(f)

tuple1 = (1, 3, 5, 6, 7)
f = isinstance(tuple1, Iterable)
print(f)

"""
迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象
特点：
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束
迭代器只能往前不会后退
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

可迭代的是不是肯定就是迭代器？
生成器是可迭代的，也是迭代器
list是可迭代的，但不是迭代器

list  ---->  迭代器
"""

list1 = [1, 2, 5, 6, 3]

list1 = iter(list1)  # 通过iter()函数将可迭代的变成了一个迭代器
print(next(list1))
# print(type(list1))
print(next(list1))


"""
迭代器定义：如果一个可迭代对象可以作为内置函数next()的实参从而支持惰性推算，那它就是一个迭代器
简便记忆：能被next()函数调用的就是迭代器，反之就不是迭代器
生成器与迭代器：
迭代器范围更大，包括生成器以及通过iter()函数变成的迭代器
"""