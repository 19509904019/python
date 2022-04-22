'''
元组与列表类似，不同之处在于元组的元素不能修改（增删改都不可以）
元组使用()，列表使用[]
定义：tuple  元组
tuple1 = ()

列表转元组： tuple(list)
元组转列表：list(tuple)

方法：count index

关键字：
    in      not in
    for ... in 
    while 
'''

# tuple1 = ()
# print(type(tuple1))

# tuple2 = ('aa')    #此时为字符串类型
# print(type(tuple2))

# tuple3 = ("a",)  #若元组中只有一个元素，必须末尾添加逗号
# print(type(tuple3))

#下标和切片,同字符串相同
tuple1 = ('a','b','c','a')
print(tuple1[0])
print(tuple1[::2])

#计数  count
count = tuple1.count('a')
print(count)

#获取下标  index
index = tuple1.index('a')   
print(index)

#添加起始位置
index = tuple1.index('a',1,4)
print(index)

