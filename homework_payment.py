"""
模拟超市付款：商品单价   商品数量
    键盘上输入商品单价，以及商品数量，然后计算应付总额
    计算应付总额  float
提示用户可以有4种付款方式
    1.现金  2.微信  3.支付宝  4.刷卡
    现金没有折扣
    微信0.95折
    支付宝  鼓励金付款金额的10%   鼓励金可以直接折算到付款金额中
    刷卡 满100-20
"""
print("欢迎来到南京财经大学超市！")

# 输入商品信息
price = float(input("请输入商品价格："))
number = int(input("请输入商品数量："))
# 计算商品总额
total = price * number
# 输入付款方式
choice = input("请输入付款方式：1.现金  2.微信  3.支付宝  4.刷卡:")
# 具体优惠方式
if choice == "1":
    print("付款总额为{0}".format(total))
elif choice == "2":
    print("微信优惠0.95折，商品总额为{0}".format(total * 0.95))
elif choice == "3":
    print("支付宝鼓励金抵扣10%，商品总额为{0}".format(total * 0.9))
elif choice == "4":
    print("刷卡支付满100-20,商品总额为{0}".format(total - total // 100 * 20))
else:
    print("输入错误，请重新输入！")

