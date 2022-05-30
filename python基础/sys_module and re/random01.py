import random

# 0-1之间的随机小数
ran = random.random()
print(ran)

# randrange(start,stop,step)
ran = random.randrange(1, 10, 2)  # 奇数
print(ran)

# 随机整数 randint(start,stop)
ran = random.randint(1, 10)
print(ran)

# 随机取字符
list1 = ['a', 'b', 'c', 'd', 'e']
ran = random.choice(list1)
print(ran)

# 打乱顺序
list2 = ['a', 'b', 'c', 'd', 'e']
random.shuffle(list2)
print(list2)


# 验证码 大小写字母与数字的组合
def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))
        # 随机取一个字符串
        r = random.choice([ran1, ran2, ran3])
        code += r
    return code


m = func()
print(m)