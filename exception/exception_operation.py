'''
Author: yujun
Date: 2022-04-03 22:20:20
LastEditors: yujun
LastEditTime: 2022-04-03 23:18:25
FilePath: \python_learning\exception\exception_operation.py
Description: 
'''
"""
格式：
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会被执行的代码]


情况1：
    try:
        有可能会产生多种异常
    except 异常的类型1:
        pass
    except 异常的类型2:
        pass

"""


def fun():
    try:
        n1 = int(input("输入第一个数字："))
        n2 = int(input("输入第二个数字："))
        answer = input("请输入运算符(+,-,*,/):")
        result = 0

        # 加法
        if answer == '+':
            result = n1 + n2
        # 减法
        elif answer == '-':
            result = n1 - n2
        # 乘法
        elif answer == '*':
            result = n1 * n2
        # 除法
        elif answer == '/':
            result = n1 / n2
        else:
            print("输入错误，请重新输入！")
        
        print("结果是：",sum)
    except ZeroDivisionError:
        print("除数不能为0！")
    
    except ValueError:
        print("必须输入数字！")

fun()
print("-----------------------------")