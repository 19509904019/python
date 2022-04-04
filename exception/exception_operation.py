'''
Author: yujun
Date: 2022-04-03 22:20:20
LastEditors: yujun
LastEditTime: 2022-04-04 10:33:20
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
        
    如果是多的except，异常类型的顺序需要注意，最大的Exception要放到最后
    
    
情况2：获取报错原因
    try:
        pass
    except Exception as e:
        print(e)  -----> e的内容就是错误的原因
        

情况3：
    try:
        有可能有异常的代码
    except 类型1：
        pass
        ...
    else:
        如果try中没有发生异常则进入的代码
        
注意：如果使用else则在try代码中不能出现return

情况4:
# 文件操作   stream = open(...)   stream.read()  stream.close()
# 数据库操作  close()
      try:
        pass
    except:
        pass
    finally:
        pass
        (close()都放在finally处)
        
"""

# 情况1
# def fun():
#     try:
#         n1 = int(input("输入第一个数字："))
#         n2 = int(input("输入第二个数字："))
#         answer = input("请输入运算符(+,-,*,/):")
#         result = 0
#
#         # 加法
#         if answer == '+':
#             result = n1 + n2
#         # 减法
#         elif answer == '-':
#             result = n1 - n2
#         # 乘法
#         elif answer == '*':
#             result = n1 * n2
#         # 除法
#         elif answer == '/':
#             result = n1 / n2
#         else:
#             print("输入错误，请重新输入！")
#
#         print("结果是：", result)
#     except ZeroDivisionError:
#         print("除数不能为0！")
#
#     except ValueError:
#         print("必须输入数字！")
#
#
# fun()


# 情况2
# def fun():
#     try:
#         n1 = int(input("输入第一个数字："))
#         n2 = int(input("输入第二个数字："))
#         answer = input("请输入运算符(+,-,*,/):")
#         result = 0
#
#         # 加法
#         if answer == '+':
#             result = n1 + n2
#         # 减法
#         elif answer == '-':
#             result = n1 - n2
#         # 乘法
#         elif answer == '*':
#             result = n1 * n2
#         # 除法
#         elif answer == '/':
#             result = n1 / n2
#         else:
#             print("输入错误，请重新输入！")
#
#         print("结果是：", result)
#     except Exception as e:
#         print("出错了，错误是：", e)
#
#
# fun()


# 情况3

# def fun():
#     try:
#         n1 = int(input("输入第一个数字："))
#         n2 = int(input("输入第二个数字："))
#         answer = input("请输入运算符(+,-,*,/):")
#         result = 0
#
#         # 加法
#         if answer == '+':
#             result = n1 + n2
#         # 减法
#         elif answer == '-':
#             result = n1 - n2
#         # 乘法
#         elif answer == '*':
#             result = n1 * n2
#         # 除法
#         elif answer == '/':
#             result = n1 / n2
#         else:
#             print("输入错误，请重新输入！")
#         # return result
#
#     except Exception as e:
#         print("出错了，错误是：", e)
#
#     else:
#         print("结果是：", result)   #此段代码不执行
#
#
# fun()


# # 情况4  此时finally处的值会覆盖前面
# def fun():
#     stream = None
#     try:
#         stream = open(r'C:\Users\Dell\Desktop\books\books.txt', 'rt', encoding='UTF-8')
#         print(stream.read())
#         return 1
#     except Exception as e:
#         print(e)
#         return 2
#     finally:
#         if stream:
#             stream.close()
#         return 3
#
#
# a = fun()
# print(a)


"""
抛出异常  raise

"""


# 注册  用户名必须6位

def register():
    username = input("输入用户名：")
    if len(username) < 6:
        raise Exception("用户长度必须6位以上！")
    else:
        print("输入的用户名是：", username)


try:
    register()
except Exception as e:
    print(e)
    print("注册失败！")
else:
    print("注册成功！")