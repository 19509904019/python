'''
while循环打印三角形
*
**
***
****
'''
"""用乘号表示  print("*"*n)"""
# count = 0
# layer = int(input("请输入打印的三角形层数："))

# while count < layer:
#     print("*"*(count+1))

#     count += 1

"""用两层while循环，一层控制行数，一层控制星星数量"""

# count_1 = 0  # 控制外层循环
# layer = int(input("请输入所要打印的行数："))

# while count_1 < layer:

#     count_2 = 0  # 控制内层循环
#     while count_2 <= count_1:
#         print("*", end=" ")
#         count_2 += 1

#     print()
#     count_1 += 1

'''
同理打印：
*****
****
***
**
*
'''
# count_1 = 0
# layer = int(input("请输入所要打印的层数："))

# while count_1 < layer :

#     count_2 = layer
#     while count_2 > count_1:
#         print("*",end=" ")
#         count_2 -= 1

#     print()    
#     count_1 += 1


'''
for循环打印上述图形
'''

layer = int(input("请输入所要打印的层数："))

# for i in range(layer):
#     for j in range(i+1):
#         print("*",end = " ")
#     print()

for i in range(layer):
    
    for j in range(layer):
        print("*",end=" ")
    layer -= 1

    print()
