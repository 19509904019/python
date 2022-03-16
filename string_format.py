'''
格式化：
1. %d %s %f.....
    print('一个 %s'%xxxx)
2.format

'''
#不使用数字填充
name = '阿燕'
age = 18
print("{}今年{}岁".format(name,age))


#使用数字填充，从0开始计数
name = '阿燕'
age = 18
print("{0}今年{1}岁,我也{1}岁".format(name,age))

#变量名的形式，format的参数必须是关键字参数
result = "{name}今年{age}岁,我也{age}岁".format(name='阿燕',age=18)
print(result)

