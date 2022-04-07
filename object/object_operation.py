"""
面向对象：
程序         现实中
对象 ---->  具体的食物

现实中事物  -----> 转成电脑程序
世间万物皆对象

好处：
1.复用
2.灵活

面向对象：
    类
    对象
    属性
    方法

对象：
    A的手机
    B的手机
    C的手机
    D的手机
    ...

    对象的集合  ----->  共同特征：品牌  颜色  大小  价格     动作：打电话  发短信  上网  玩游戏
    类别：手机类
        学生类
    特征：姓名  年龄  性别  身高  血型  ....   -----> 属性
    动作：刷微博  刷抖音  发动态  ....   ---->方法

    多个对象  --->  提取对象的共同特征和动作  ---->  封装到一个类中

定义：
    class 类名(父类):
        属性：特征
        方法：动作

"""
# # 所有的类名要求首字母大写，多个单词使用驼峰式命名
# # ValueError  TypeError  StopIterable
# # 默认继承object
# class Phone:
#     # 属性
#     brand = 'HUAWEI'
#     # 方法
#     pass
#
#
# # 使用类创建对象
# ayan = Phone()
# print(ayan.brand)
# 改变属性
# ayan.brand = 'iPhone'
# print(ayan.brand)

# yjun = Phone()
# print(yjun.brand)

"""
定义类和属性
"""
# # 定义类
# class Student:
#     # 类属性
#     name = 'ayan'
#     age = 18

# 使用类
# yanyan = Student()
# # yanyan.age = 3  # 对象属性
# # 先找自己空间的，然后再去模型中去找，如果自己空间中存在age属性，则不会去模型中去找
# print(yanyan.age)
# # 更改类属性
# Student.age = 20
# print(yanyan.age)
# # 新的对象也是改过后的类属性
# yujun = Student()
# print(yujun.age)

"""
类中的方法：动作
种类：普通方法  类方法  静态方法  魔术方法
"""

"""
普通方法格式：
def 方法名(self,[参数,参数]):
    pass
"""
# class Phone:
#     brand = 'HUAWEI'
#     price = 5999
#     type = 'P40'
#
#     # Phone类里面的方法:call
#     def call(self):
#         print("self----->",self)   #self就是调用类创建的对象本身
#         print("正在打电话...")
#         print("留言：",self.note)
#
#
# phone1 = Phone()
# print(phone1,"-----1-----")   #将对象自身作为类中方法的参数
# phone1.note = 'phone1的note'
# phone1.call()
#
# print("*"*30)
# phone2 = Phone()
# print(phone2,"-----2-----")
# phone2.call()    #对象没有类中方法的属性就会报错


"""
函数 和 类里面定义的函数：方法
"""
# def func(names):
#     for name in names:
#         print(name)
#
# username = ['yujun','ayan','yanyan']
# func(username)


# class Phone:
#     # 魔术方法之一:称作魔术方法  __名字__()
#     def __init__(self):  # init 初始化
#         """
#         动态的给self空间添加了两个属性：brand,price
#         """
#         self.brand = 'huawei'
#         self.price = 4999
#
#     def call(self):   # self是不断发生改变的
#         print("------>call")
#         print("价格：",self.price)   # 不能保证每个self中都存在price


# p = Phone()
# p.price = 1000
# p.call()   # p.call()  p是一个对象，在电脑中是一块地址

'''
1.找有没有一块空间是Phone
2.利用Phone类，向内存申请一块Phone一样空间
3.去Phone中找有没有__init__
    如果没有则执行将开辟内存给对象名：p
    如果有__init__,则会进入init方法执行里面动作,将内存地址赋值给对象p
'''

# p = Phone()
# p.call()
#
#
# p1 = Phone()
# p1.price = 5999
# p1.call()

#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # def eat(self):
#     #     print("{}正在吃红烧肉...".format(self.name))
#
#     # 也可以对方法传送参数
#     def eat(self, meat):
#         print("{}正在吃{}...".format(self.name, meat))
#
#
# # 自定义参数
# p = Person("yujun", 18)
# p.eat('红烧肉')
#
# p1 = Person('', 18)
# p1.name = '王五'
# p1.eat('红烧肉')


"""
类方法

特点：
    1.定义需要依赖装饰器@classmethod
    2.类方法中参数不是一个对象，而是类
        print(cls)  --->  <class '__main__.Dog'>
    3.类方法中只可以使用类属性
    4.类方法中可否使用普通方法？  不能

类方法作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作(功能)
只能用类的，不能用对象的
"""

# class Dog:
#     #初始化
#     def __init__(self,name):
#         self.nane = name
#
#     def run(self):
#         print("{}在院子里跑来跑去".format(self.nane))
#
#     @classmethod
#     def test(cls):
#         print(cls)
#         # print(cls.name)   # 报错
#
#
# # d = Dog("豆豆")
# # d.run()
# Dog("豆豆").run()
#
# Dog.test()


# 补充类方法
"""
静态方法：很类似类方法
1.需要装饰器@staticmethod
2.静态方法是无需传递参数（cls,self）
3.也只能访问类的属性和方法，对象是无法访问的
4.加载时机同类方法

总结：
类方法   静态方法
不同：
1.装饰器不同
2.类方法有参数，静态方法无参数

相同：
1.只能访问类的属性和方法，对象是无法访问的
2.都可以通过类名调用访问
3.都可以在创建对象之前使用，因为是不依赖于对象

普通方法 与两者区别：
不同：
1.没有装饰器
2.普通方法永远是要依赖对象，因为每个普通方法都有一个self
3.只有创建了对象才可以调用普通方法，否则无法调用

"""

# class Person:
#     __age = 18
#
#     def show(self):
#         print('----->', Person.__age)
#
#     @classmethod
#     def update_age(cls):
#         cls.__age = 20
#
#     @classmethod
#     def show_age(cls):
#         print("更新后的年龄是:", cls.__age)
#
#
#
# Person.update_age()
# Person.show_age()


'''
魔术方法
__init__:初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）

__new__:实例化魔术方法
在实例化时触发,开辟一个新空间

new开辟空间意思就是创建对象
init是初始化对象
new + init 才是完整的构造器

在__new__()方法中要 return 地址给__init__(),重写必须需要返回值

__call__:调用对象的魔术方法
触发时机：将对象当成函数使用的时候，会默认调用此函数中的内容
p = Person()
p()

__del__:析构魔术方法
触发时机：当对象没有用（没有任何变量引用）的时候被触发

1.对象赋值
p = Person()
p1 = p
说明：p和p1共同指向同一个地址

2.删除地址的引用
del p1  删除p1对地址的引用

3.查看对地址的引用次数

4.当一块空间没有了任何引用，默认执行__del__()
程序执行完毕后，python解释器回收所有在本次执行过程中使用到的空间，所以最后执行__del__()

__str__
触发时机：打印对象名  自动触发去调用__str__里面的内容
注意：一定在__str__()方法中添加return，return后面的内容就是打印对象看到的内容
'''
# import sys


# class Person:
# def __init__(self, name):
# print("-----init------", self)  # <__main__.Person object at 0x0000025BB8D954F0>
# self.name = name

# def __new__(cls, *args, **kwargs):  # __new__向内存要空间  ---> 地址
#     print("----new------")
#     # return super().__new__(cls)  # super()调用父类方法一般不用传参
#     position = object.__new__(cls)  # <__main__.Person object at 0x0000025BB8D954F0>
#     print(position)
#     return position

# def __call__(self, *args, **kwargs):
#     print("------->call")

# def __call__(self, name):
#     print("------->call", name)
#
# def __del__(self):
#     print("程序结束啦！！！")
#
# def __str__(self):
#     return '姓名是：' + self.name + '，年龄是：18'


# __new__
# p = Person("yanyan")
# # print(p.name)   __new__将前面的魔术方法覆盖重写了
# print(p)  # <__main__.Person object at 0x0000025BB8D954F0>

# __call__
# p = Person("yanyan")
# p(123)


# __del__
# p = Person('yanyan')
# p1 = p
# p2 = p
# print(sys.getrefcount(p))
#
#
# del p1
# print(sys.getrefcount(p))
#
# del p2
# print(sys.getrefcount(p))
# print(p.name)

# __str__
# p = Person('yanyan')
# print(p)


'''
总结：魔术方法

重点：
__init__  (构造方法，创建完空间之后调用的第一个方法)
__str__

了解：
__new__  作用：开辟空间

__del__  作用：没有指针引用的时候会调用，99%都不需要重写

__call__ 作用：想不想当成函数用

大总结：
方法：
    普通方法  ---->  重点
    def 方法名(self,[参数]):
        方法体
    
    对象.方法()
    
    方法之间的调用：
    class A:
        def a(self):
            pass
        def b(self):
            #调用a方法
            self.a()
            
    类方法:
    @classmethod
    def 方法名(cls,[参数]):
        pass
        
    类名.方法名()
    对象.方法名()
          
    静态方法:
    @staticmethod
    def 方法名([参数]):
        pass
        
    类名.方法名()
    对象.方法名()
    
    魔术方法:自动执行方法
    print(p)  ---->  __str__
    
'''
