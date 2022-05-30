'''
集合：
set
特点：没有重复，无序的(没有下标)
符号：{} {元素，元素，元素，....}   -----> 集合
     {}  }{key:value,key:value....}  -----> 字典
'''

# set = {'ayan'}
# print(type(set))  #<class 'set'>

# list = [1,2,3,3,4,4,5,3,6,0]
# list = set(list)
# print(list)



'''
append  extend  insert  ----->  list
add  update  ----->set

list:有序，允许重复
set:无序，不允许重复
'''
# # 添加元素  add
# set1 = set()
# set1.add("三体")
# print(set1)

# result = set1.add("三体")
# print(set1)
# print(result)


'''
删除：remove()   discard()
del set : 删除整个集合
pop():随机删除集合中任意一个元素
'''

# set1 = {'1','2','3','4','5'}
# print(set1)

# set1.remove('1')
# print(set1)
# # set1.remove('6')  #报错  keyErrorr
# # print(set1)

# set1.discard('2')  
# print(set1)
# set1.discard('2')  #没有元素时，不报错
# print(set1)

'''
交集(&)：intersection
并集(|)：union
差集(-)：difference
'''

set1 = {0,1,2,3,4,5}
set2 = {4,5,6,7,8,9}

result = set1.difference(set2)
print(result)
result = set1.union(set2)
print(result)
result = set1.intersection(set2)
print(result)