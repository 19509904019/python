'''
替换内容：replace(old,new,count)  默认全部替换，也可以通过count指定次数
切割字符串：split,rsplit,splitlines,partition,rpartition
split('分隔符',maxsplit)  返回的结果是一个列表,maxsplit 最多的分割次数
partition 括号中的分隔符是字符串中的字符
修改大小写：capitalize,title,upper,lower


'''
#替换内容  替换红豆相思  正则表达式  循环+列表  


# string = '红豆生南国，春来发几枝。愿君多采撷，此物最相思。--- <相思>'
# result = string.replace('相思','xiangsi',1)
# print(result)

# string = '红豆 相思 君'
# result = string.split(' ',1)
# print(result)
# result = string.rsplit(' ',1)
# print(result)
# #splitlines按行分割
# string = '''红豆
# 相思
# 君'''
# result = string.splitlines()
# print(result)

# #partition 括号中的分隔符是字符串中的字符
# string = '红豆,相思 君'
# result = string.partition(',')
# print(result)


'''
空格处理：ljust,rjust,center,lstrip,rstrip,strip
strip:去除字符串当中的空格
lstrip:只去除左边字符串的空格
rstrip:只去除右边字符串的空格    # 删除字符串左侧或者右侧的空格
center:通过空格调整对齐
ljust:左对齐 
rjust:右对齐  #添加空格使左侧、右侧或者居中对齐

字符串拼接：join

比如用户在注册用户名时多打了一个空格造成错误，解决这个问题
'''
#删除空格
# string = ' admin    '
# print(len(string))
# result = string.strip()
# print(len(result),result)



#添加空格使对齐
# string = 'admin'
# result = string.center(20)
# print(result)

