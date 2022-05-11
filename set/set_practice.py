'''
产生5组（不允许重复），字母和数字组成4为验证码
最终打印此5组验证码
'''
# 11111  五组不同内容的验证码
import random

# # 存放所有验证码
# numbers = []
# # 验证码字符串
# string = '0123456789qwertyuiopasdfghjklzzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# # 生成五组验证码
# for i in range(5):
#     # 初始化
#     number = set()
#     # 生成验证码
#     while len(number) < 4:
#         number.add(string[random.randint(0, len(string) - 1)])
#     numbers.append(number)

# print(numbers)
# # 打印输出
# for i in numbers:
#     print(''.join(i), end=' ')

# #2222  不同的五组验证码
# import random
# #存放所有验证码
# all_code = set()
# #验证码字符串
# string = '0123456789qwertyuiopasdfghjklzzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# while True:
#     #初始化验证码
#     codes = ''
#     for i in range(4):
#         codes += string[random.randint(0,len(string)-1)]
#     all_code.add(codes)
#     #判断长度
#     if len(all_code) == 5:
#         print(all_code)
#         break

import random

# 存放所有验证码
all_code = set()
# 验证码字符串
string = '0123456789qwertyuiopasdfghjklzzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

while len(all_code) < 5:
    # 初始化验证码
    codes = ''
    for i in range(4):
        codes += string[random.randint(0, len(string) - 1)]
    all_code.add(codes)
# 打印输出
print(all_code)
