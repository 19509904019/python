'''
买多件商品
商品名称，价格，数量，总价
要用到列表的嵌套
'''
# #添加商品信息
# container = []
# #商品总价
# count = 0
# while True:
#     #输入商品信息
#     name = input("请输入商品名称：")
#     price = input("请输入商品价格：")
#     number = input("请输入商品数量：")
#     #存放商品信息
#     goods = [name,price,number]
#     container.append(goods)
#     answer = input("是否继续添加商品？（按任意键继续，按Q或q退出！）:")
#     #判断继续条件
#     if answer.lower() == 'q':
#         print("退出成功！")
#         break

# #分割符
# print('-'*50)
# print("您的购物清单如下\n")
# print("名称\t价格\t数量")
# #打印商品信息
# for message in container:
#     print("{}\t{}\t{}".format(message[0],message[1],message[2]))
#     count = count + float(message[1])*float(message[2])
# print()
# #打印商品总价
# print("您需付款的金额为：%.2f" % count)


'''
生成8个1-100之间的随机整数，保存到列表中，
键盘输入一个1-100之间的整数，将整数插入到排序后的列表中（升降没有要求）
'''
# import random
# # 保存随机整数
# numbers = []
# # 随机取数
# numbers = random.sample(range(1, 100), 8)
# # 对数据进行排序
# numbers.sort()
# # 打印数据
# print("随机成的数据为：{}".format(numbers))
# while True:
#     number = int(input("请输入一个1-100之间的整数："))
#     # 将数据在列表当中排序
#     if 1<=number<=100:
#         #添加到列表当中
#         numbers.append(number)
#         #重新排序
#         numbers.sort()
#         print("重新排序的列表为：{}".format(numbers))
#         break
#     else:
#         print("输入错误，请重新输入!")


'''
冒泡排序
'''