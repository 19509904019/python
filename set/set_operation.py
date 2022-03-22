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
# 添加元素  add
set1 = set()
set1.add("三体")
print(set1)

result = set1.add("三体")
print(set1)
print(result)