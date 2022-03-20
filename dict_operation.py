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

#改变年龄   键是不能修改的，可以添加和删除，但后面的值可以修改
dict['age'] = 17
print(dict)