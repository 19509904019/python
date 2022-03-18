'''
如何定义一个列表
1.空列表：[]
2.有内容的列表：['A','B','C'],[1,2,3,4],[3.5,4.2,5.2]....

数据类型：
int float str bool  list  ...
列表里面还可以套列表
'''
# #定义一个空列表
# list1 = []

# #定义一个非空列表
# list2 = ['牛奶','面包','火腿肠','辣条','臭豆腐','食盐','方便面']

# #获取列表里面的元素，通过索引（下标）
# print(list2[2])

# #臭豆腐面包
# result = list2[-3::-3]
# print(result)

# #食盐 辣条
# result = list2[5:2:-2]
# print(result)

# #牛奶 辣条 臭豆腐
# # print(list2[:4:3])
# list = []
# index = [0,3,4]  #索引查找
# for i in index:
#     list.append(list2[i])
# print(list)
# #跟上式等价
# # list = [list2[i] for i in index]
# # print(list)

'''
s = 'abc123'

for i in range(n)
或
for i in s
'''

'''
添加  删除  修改  查询
1. 添加元素  append 追加  类似排队
'''
# list1 = []
# list1.append("火腿肠")
# print(list1)

'''
数字 n = 1+2
字符串  s = 'a'+'b'  ----> ab
列表  list = [1,2,3] + ['a','b']
列表也可以用 + 来连接
初除此之外，还可以用extend
'''
# list = [1,2,3] + ['a','b']
# print(list)

# list1 = [1,2,3]
# list2 = ['a','b']
# list1.extend(list2)
# print(list1)

'''
删除：pop  remove  clear
pop(index):根据下标删除列表中的元素，下标在写的时候不要超出范围
如果不添加任何参数，则默认从后往前删除，先进后出（栈）

remove(element):根据元素名称删除，元素要存在删除的列表当中
如果列表中存在多个同名元素，只删除第一个元素，后面的元素不会被删除

关键字in: 元素 in 列表 
'''
list = ['面包', '辣条','辣条', '方便面', '火腿肠']
# # 判断元素是否在列表当中
# if '辣条啊' in list:
#     print("yes")
# else:
#     print("no")

# for循环  删除重复元素要遍历list[:]
#list和list[:]是两个不同的空间，所以删除和遍历会分别在两个列表进行
# for string in list[:]:
#     if string == '辣条':
#         list.remove('辣条')
# print(list)

# list1 = []
# for string in list:
#     if string != '辣条':
#         list1.append(string)
# print(list1)


for string in range(list.count('辣条')):
    list.remove('辣条')
print(list)
#while循环用于不确定次数的循环
##第一种
# while '辣条' in list:
#     list.remove('辣条')
# print(list)

#第二种
# n = 0
# while n < len(list):
#     if list[n] == '辣条':
#         list.remove('辣条')
#     else:
#         n += 1
# print(list)

'''
修改
insert(index,element)：按index插入元素
replace(old,new,count):按原来的元素替换新元素
index(element):根据元素找该元素的位置下标，返回值是下标
'''
