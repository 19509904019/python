"""
猜拳游戏： 3局
剪刀：0  石头：1  布：2
三局两胜

"""

import random

# 计数
c_count = 0  # 计算机赢的次数
p_count = 0  # 人赢的次数
count = 0  # 猜拳次数
while count <= 2:
    # 猜拳
    computer = random.randint(0, 2)
    guess = int(input("请输入剪刀（0） 石头（1） 布（2）："))  # 输入你想出的数
    count += 1

    # 比胜负
    if (computer == 2 and guess == 0) or (computer == 2 and guess == 1) or (computer == 1 and guess == 0):
        print("很遗憾，您输了...")
        c_count += 1
    elif (computer == 0 and guess == 2) or (computer == 1 and guess == 2) or (computer == 0 and guess == 1):
        print("太棒了，您赢了...")
        p_count += 1
    else:
        print("打平了...")

print()
# 判断结果
if c_count > p_count:
    print("最终您输了")
elif c_count < p_count:
    print("最终您赢了")
else:
    print("最终打平了")
