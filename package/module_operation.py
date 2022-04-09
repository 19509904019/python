'''
模块

python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件（.py）就是一个模块（module）
模块名就是文件名去掉后缀py。这样做的好处是：
1.提高代码的可复用、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
2.解决了命名冲突，不同模块中相同的命名不会冲突

模块：
1.自定义模块
2.使用系统一些模块

导入模块：
1.import 模块名
    模块名.变量  模块名.函数  模块名.函数

2.from 模块名 import 变量/函数/类
同一模块导入多个时，在import后用逗号隔开

3.from 模块名 import *
该模块中所有的内容
但是如果想限制获取的内容，可以在模块中使用__all__ = [(使用*可以访问到的内容)]

4. 无论上述哪两种形式，都会将模块中的内容进行加载
   如果不希望其进行调用，就会用到__name__
   在自己的模块里面__name__叫：__main__
   如果在其他模块中通过导入的方式调用的话：__name__是模块名
'''
# 导入模块
import calculate

# 使用模块中的函数  模块名.变量  模块名.函数  模块名.函数
list1 = [1, 2, 4, 5, 7, 7]
sum = calculate.add(*list1)
print(sum)

cal = calculate.Calculate(0)
cal.test1()
# cal.test2()
# 类方法无需创建对象即可调用
calculate.Calculate.test2()

# 导入某一部分
from calculate import add

list1 = [1, 2, 4, 3, 6, 4, 2, 9]
result = add(*list1)
print(result)
