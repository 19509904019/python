"""
文件夹  包
文件夹：非py文件
包：含有__init__.py文件

一个包中可以存放多个模块

项目 > 包 > 模块 > 类  函数  变量


目录同级：
 from 包 import 模块
 from 包.模块 import 类|函数|变量
 from .模块 import 类|函数|变量
"""

'''
__init__.py 文件
当导入包的时候，默认调用__init__.py文件
作用：
1.当导入包的时候，把一些初始化的函数、变量、类定义在__init__.py文件中
2.此文件中函数、变量等的访问，只需要通过包名.函数...
3.结合__all__ = [通过 * 可以访问的模块]

from 模块 import *
表示可以使用模块里面的所有内容，如果没有定义__all__所有的都可以访问
但是如果添加上了__all__,只有__all__ = ['',''] 列表中可以访问


from 包 import *
不可以使用包里面的所有内容，需要在__init__.py 文件中定义 __all__ = ['','']
此时可以访问__all__中的内容

'''
import user
from user import *

user.creat_app()
user.printA()

# __all__ = ['a']  a可以调用而b不可以调用
a.show()
# b.show()