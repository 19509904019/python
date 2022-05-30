"""
分组
匹配数字0-100数字

"""
import re

n = '100'

# result = re.match(r'\d?\d$', n)
# print(result)

# 改进版
result = re.match(r'[1-9]?\d$|100$', n)
print(result)

# (word | word | word) 区别 [abc]表示的是一个字母而不是一个单词
# 验证输入的邮箱  163 126 qq
email = '1241412075@qq.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.com$', email)
print(result.group())

# 不是以4、7结尾的号码（11位）
phonre_number = '19509904019'
result = re.match(r'1\d{9}[01235689]$', phonre_number)
print(result.group())

# 爬虫
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result)

# 分别提取
print(result.group())
# ()表示分组，group(1)表示提取到第一组的内容   group(2)表示提取到第二组的内容
print(result.group(1))
print(result.group(2))

#
msg = '<html>abc</html>'
msg1 = '<h1>hello</h1>'
result = re.match(r'<.+>(.+)<.+>$', msg1)
print(result)
print(result.group(1))

result = re.match(r'<([a-zA-Z0-9]+)>(.+)</\1>$', msg)
print(result)
print(result.group(2))

#
msg = '<html><h1>abc</h1></html>'
result = re.match(r'<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.+)</\2></\1>', msg)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))

