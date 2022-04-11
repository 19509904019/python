"""
1.正则表达式的定义
正则表达式是对字符串（包括普通字符（如a-z）和特殊字符（元字符））操作的一种逻辑公式，就是用事先定义好的一些特定字符及这些特定字符的组合，组成一个“规则字符串”，
这个“规则字符串”用来表达对字符串的一种过滤逻辑

2.正则表达式的作用和特点
给定一个正则表达式和另一个字符串，我们可以达到如下目的：
（1）给定的字符串是否符合正则表达式的过滤逻辑（称作”匹配“）
（2）可以通过正则表达式，从字符串中获取我们想要的特定部分

正则表达式的特点：
1.灵活性、逻辑性和功能性非常强
2.可以迅速的用极简单的方式达到字符串的复杂控制
3.对于刚接触的人来说，比较晦涩难懂

场景：
任何判断一个字符串是手机号码？

判断邮箱为163或者162的所有邮件地址



python中提供了 re模块：


"""
# 普通判断
# QQ = input("请输入QQ号码：")
#
# if len(QQ) >= 5 and not QQ.startswith('0'):
#     print("合法的！")
#
# else:
#     print("不合法的！")

import re

# 使用正则re模块方法：match

s = '迪丽热巴古力娜扎蒋欣'

result = re.match("蒋欣", s)  # 只要从开头进行匹配，如果匹配不成功就返回None
print(result)

result = re.search("蒋欣", s)  # search 进行正则字符串匹配方法，匹配的是整个字符串
print(result)
print(result.span())  # 返回位置
print(result.group())  # 使用group提取到匹配的内容
print(result.groups())

print()
print('-' * 50)
print()

# s = '哈哈2'
# result = re.search('[12345]', s)
# print(result)
msg = 'srfetg16rtgewg23'

result = re.search('[a-z][0-9]', msg)  # search 只要有匹配的后面就不会继续进行检索，找到一个匹配的就会停止

print(result.group())

result = re.findall('[a-z][0-9]', msg)  # findall匹配整个字符串，找到一个继续向下找，一直到字符串结尾
print(result)
'''
正则符号
1.[]表示是一个范围
2."."用于匹配除换行符（\n）之外的所有字符
3."^"用于匹配字符串的开始，即行首
4."$"用于匹配字符串的末尾（末尾如果有换行符\n，就匹配\n前面的那个字符），即行尾
定义正则验证次数：
5.* 用于将前面的模式匹配0次或多次（贪婪模式，尽可能多的匹配）   x>=0
6.+ 用于将前面的模式匹配1次或多次（贪婪模式）   x>=1
7.？ 用于将前面的模式匹配0次或1次（贪婪模式）   x = 0 or 1
8.*？ +？ ？？ 即上面三种特殊字符的非贪婪模式（尽可能少的匹配）
9.{m} 用于验证将前面的模式匹配m次
10.{m,n} 用于将前面的模式匹配m次到n次（贪婪模式），即最小匹配m次，最大匹配n次  m<x<n
11.{m,n}? 即上面{m,n} 的非贪婪版本
'''
msg = "agvaggfgva45645468fdsfdfgdl2gdg43sfag"

result = re.findall('[a-z][0-9]+[a-z]', msg)
print(result)

result = re.findall('[a-z][0-9]*[a-z]', msg)
print(result)

result = re.findall('[a-z][0-9]?[a-z]', msg)
print(result)

#QQ号验证
QQ = '1241412075'
result = re.match('^[1-9][0-9]{4,10}$',QQ)
print(result)
