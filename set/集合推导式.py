'''
Author: yujun
Date: 2022-04-05 09:03:00
LastEditors: yujun
LastEditTime: 2022-04-05 10:46:48
FilePath: \python_learning\set\集合推导式.py
Description:  
'''
'''
集合推导式  [] ----> {}
重复项会去除
'''

set1 = {i for i in range(10) if i % 2 == 0}
print(set1)