"""
掷骰子（两个）
1.玩游戏要有金币，没有金币则不能玩     √
2.玩游戏赠送金币一枚，充值获取金币     √
3.只能充值10的倍数，如果不是则充值不了，10元20个     √
4.玩游戏消耗5金币   √
5.猜大小：猜对  鼓励金币2枚
        猜错  没有奖励
    （两个骰子超出6则称为大，否则小）   √
6.游戏结束 ： （1）主动退出 （2）没有金币退出
7.退出则打印金币数，共玩了几局  √
"""
import random

coins = 0  # 记录金币数
total = 0  # 记录两个骰子总数和
count = 0  # 记录玩的局数

if coins < 5:
    # 金币不足，先充值金额
    print("金币数不足，请先充值！")
    while True:
        money = int(input("请输入充值金额："))
        # 判断充值金额是否正确：只能充值10的倍数，如果不是则充值不了，10元20个
        if money % 10 == 0 and money > 0:
            coins += money // 10 * 20
            print("充值成功，您充值的金额为%d,剩余金币数为%d" % (money, coins))
            # 判断是否继续充值
            recharge = input("是否继续充值(y/n):")
            if recharge == 'n':
                print("充值结束！")
                break
        else:
            print("充值金额错误，请重新充值!")

    # 金币充足，开始游戏
    while answer == 'y' and coins > 5:
        print("-------欢迎进入掷骰子游戏------------")
        answer = input("是否进入游戏(y/n):")
        # 玩游戏赠送金币
        coins += 1
        # 每局游戏扣除金币
        coins -= 5
        # 设置两个随机数进行掷骰子猜大小
        rand1 = random.randint(1, 6)
        rand2 = random.randint(1, 6)
        total = rand1 + rand2
        # 你猜的数
        guess = input("请输入你猜的结果(大/小):")
        # 判断是否猜对
        if (guess == '大' and total > 6) or (guess == '大' and total <= 6):
            print("恭喜你猜对了,获得金币两枚！")
            coins += 2
        elif guess != '大' and guess != '小':
            print("请输入正确的结果(大/小)")
        else:
            print("很遗憾，您猜错了！")

        # 记录局数
        count += 1
        answer = input("是否继续游戏(y/n):")


    print("游戏结束,您一共玩了%d局,剩余金币数为%d枚。" % (count, coins))
