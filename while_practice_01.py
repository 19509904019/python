"""

超市购物付款

"""

total = 0
sum = 0
while True:
    price = float(input("请输入商品的价格："))
    number = int(input("请输入商品的数量："))

    total += price * number
    sum += number
    answer = input("当前的商品总额为%.2f,是否退出当前结算页面(按“q”键结束,“s”键继续):" % total)
    if answer == 'q':
        break

print("共买了%d件商品，商品的总价格为%.2f" % (sum, total))
