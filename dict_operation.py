'''
结构:{键1：值，键2：值，键3：值}
字典：{}
元素：键值对  注意：键是唯一的，值是允许重复的

下标  或者  切片 ------->   没有

操作：
1.添加元素：
字典名[key] = value
注意：key是唯一的，所以在添加的时候如果出现同名的key,后面key对应的value则替换原来的


'''
dict1 = {}
print(type(dict1))

dict1['name'] = '阿燕'
dict1['gender'] = '女'
dict1['age'] = 18
print(dict1)