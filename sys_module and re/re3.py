import re
import requests

# 起名的方式
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result)

"""
分组：（）    ---->   result.group(1)  获取组中匹配内容
不需要引用分组的内容：
    result = re.match(r'<([a-zA-Z0-9]+)>(.+)</\1>$', msg)
    print(result)
    print(result.group(2))
    
引用分组匹配内容：
    1.number  \number 引用第number组的数据
        msg = '<html><h1>abc</h1></html>'
        result = re.match(r'<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.+)</\2></([a-zA-Z0-9]+)>', msg)
        print(result)
        
    2.名字 ?P<name1>
        msg = '<html><h1>abc</h1></html>'
        result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
        print(result)
        

re模块：
match  从开头匹配一次
search  只匹配一次
findall  查找所有
sub(正则表达式，"新内容"，string) 替换
split 在字符串中搜索遇到[]中的符号就分割
"""

result = re.sub(r'\d+', '98', 'java:100,python:100')
print(result)  # java:98,python:98


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r'\d+', func, 'java:100,python:100')
print(result)

msg = 'java:98,python:98'
result = re.split(r'[:,]', msg)
print(result)

"""
默认是贪婪的，如果想将贪婪模式变成非贪婪模式 加上？
"""

msg = 'abc123abc'

result = re.match(r'abc(\d+)', msg)
print(result)

result = re.match(r'abc(\d+?)', msg)
print(result)

path = '<img src="https://t1.chei.com.cn/axvert/img/3671010113.jpg" width="490" height="260">'

# result = re.match(r'<img src="(.+\.jpg)"', path)
result = re.match(r'<img src="(.+?)"', path)
# print(result.group(1))

image_path = result.group(1)
print(image_path)
response = requests.get(image_path)

with open('aa.jpg', 'wb') as wstream:
    wstream.write(response.content)
