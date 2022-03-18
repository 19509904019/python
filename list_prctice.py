'''
买多件商品
商品名称，价格，数量，总价
要用到列表的嵌套
'''
#添加商品信息
container = []
#商品总价
count = 0
while True:
    #输入商品信息
    name = input("请输入商品名称：")
    price = input("请输入商品价格：")
    number = input("请输入商品数量：")
    #存放商品信息
    goods = [name,price,number]
    container.append(goods)
    answer = input("是否继续添加商品？（按任意键继续，按Q或q退出！）:")
    #判断继续条件
    if answer.lower() == 'q':
        print("退出成功！")
        break

#分割符
print('-'*50)
print("您的购物清单如下\n")
print("名称\t价格\t数量")
#打印商品信息
for message in container:
    print("{}\t{}\t{}".format(message[0],message[1],message[2]))
    count = count + float(message[1])*float(message[2])
print()
#打印商品总价
print("您需付款的金额为：%.2f" % count)

