"""
产生随机数(1-20)
可以猜多次，直到猜对为止，如果猜错了适当给出提示，猜大了还是猜小了
1.统计猜了几次
2.如果一次就中：简直欧皇附体，一次就中了
    2-5次：运气还可以噢
    6次以上：猜对了，但运气一般噢
"""

import random

count = 0
guess = random.randint(1, 20)

while True:
    number = int(input("请输入你猜的数(范围在1到20):"))
    count += 1
    if 0 < number <= 20:
        if number > guess:
            print("你猜的数字大了！")
        elif number < guess:
            print("你猜的数字小了！")
        else:
            if count == 1:
                print("简直太棒啦，一次就猜对了！")
            elif 1 < count < 6:
                print("猜对啦，您猜了%d次，运气还可以噢！" % count)
            else:
                print("猜对啦，您猜了%d次，运气很一般噢！" % count)
            break
    else:
        print("输入的数字有误，请重新输入一个1-20的数字！")
