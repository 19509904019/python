# 列表推导式：最终得到的是一个列表

# list = []
# for i in range(1,21):
#     list.append(i)
# print(list)

# 格式1
# list = [i for i in range(1,21)]
# print(list)

# 将 1-100之间所有的偶数存放到列表当中
# list = [i for i in range(2,101,2)]
# print(list)

# #格式2  if判断放后面
# list = [i for i in range(1,101) if i%2==0]
# print(list)

# 取出英文字符
# list = ['1','hello','2','world','3','5']
# list1 = [i for i in list if i.isalpha()]
# print(list1)

# #格式3 [结果1 if 条件 else 结果2 for 变量 in 可迭代的]
# #如果是h开头的则将首字母大写，不是h开头的全部转为写
# list2 = [i.title() if i.startswith('h') else i.upper() for i in list]
# print(list2)

# #格式4 两层for循环
# list3 = [(i,j) for i in range(1,3) for j in range(1,3)]
# print(list3)


# # 请写出一段 python 代码实现分组一个list里面的元素，比如[1,2,3,4....100]变成[[1,2,3],[4,5,6]...] :切片
# a = [i for i in range(1,101)]
# # print(a)
# b = [a[i:i+3] for i in range(0,len(a),3)]  #巧妙利用步长和切片
# print(b)

# c = [[i,i+1,i+2] if i < 98 else [j for j in range(i,101)] for i in range(1,101,3)]

# 找出里面名字含有两个 'e' 的放到新列表中：
# names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe']
#          ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]

# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# new_names = [j for i in names for j in i if j.count('e') == 2]
# print(new_names)
#

# 0~5偶数  0~10奇数
# [(偶数，奇数)，（）...]   [(0,3),(0,5),(0,7)....]

# newlist = [(i, j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 2 != 0]
# print(newlist)
