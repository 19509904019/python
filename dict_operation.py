'''
结构:{键1：值，键2：值，键3：值}
字典：{}
元素：键值对  注意：键是唯一的，值是允许重复的

下标  或者  切片 ------->   没有

操作：
1.添加元素：
字典名[key] = value
注意：key是唯一的，所以在添加的时候如果出现同名的key,后面key对应的value则替换原来的

2.修改value值
字典名[key] = value

关键看key:如果字典中不存在键，则是添加
         如果字典中存在键，则是修改
'''
dict = {}
print(type(dict))

dict['name'] = '阿燕'
dict['gender'] = '女'
dict['age'] = 18
print(dict)

# 改变年龄   键是不能修改的，可以添加和删除，但后面的值可以修改
# dict['age'] = 17
# print(dict)

''''
字典删除：
pop(key):删除的是键值对，返回值key对应的value
popitem():返回值(key,value)  从后往前删内容
'''
# dict.pop('age')
# print(dict)

# a = dict.popitem()
# print(a)
# print(dict)


'''
遍历和查询：
列表：list.index()   list.count()    in 

获取：
dict.get(key)  根据key获取value值
dict[key]
区别：get(key)里面的key如果不存在则返回None，同时get(key,默认值)可以设置默认值
     dict[key] 会报error错误


如果使用for...in...直接遍历字典，取出的是字典的key
for i in dict:
    print(i)

获取字典中所有的key值：字典.keys()
获取字典中所有的value值：字典.values()

'''
#根据key得到value值  get不会报错
# value = dict.get('age')
# print(value)


for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)
