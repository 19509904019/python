"""
题目：
车（Car）:
属性：车名，时速
方法：1.求车名在那条公路上多少时速行驶了多长
        get_time(self,road)
     2.初始化车属性信息__init__方法
     3.打印对象显示车的属性信息
"""
# import random
#
#
# # 公路类
# class Road:
#     def __init__(self, name, len):
#         self.name = name
#         self.len = len
#
#
# # 汽车类
# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#
#     def get_time(self, road):
#         rand_time = random.randint(1, 10)
#         msg = '{}在{}上以{}km/h行驶{}小时'.format(self.brand, road.name, self.speed, rand_time)
#         print(msg)
#
#     def __str__(self):
#         return '{}的速度为{}'.format(self.brand, self.speed)
#
#
# # 创建实例化对象
# road = Road("铜无高速", 200)
#
# BMW = Car('宝马X3', '90')
# # print(BMW)
# BMW.get_time(road)  # 将生成的对象作为参数


'''
is a  |  has a 

student  book  computer

知识点：
1.has a
    一个类中使用了另外一种自定义的类型
    例如一个方法中使用了另一个对象作为参数
    
    student使用了computer book
    
2.类型
    系统类型：
     str int float
     list dict tuple set
     
     自定义类型：
        创建的对象等等
        算是自定义类型，都可以将其当成一种类型
'''

# class Book:
#     def __init__(self, bookname, author, number):
#         self.bookname = bookname
#         self.author = author
#         self.number = number
#
#     def __str__(self):
#         return self.bookname + '---' + self.author + '---' + str(self.number)
#
#
# class Computer:
#     def __init__(self, brand, type, color):
#         self.brand = brand
#         self.type = type
#         self.color = color
#
#     def online(self):
#         print("正在使用电脑上网...")
#
#     def __str__(self):
#         return self.brand + '----' + self.type + '----' + self.color
#
#
# class Student:
#     def __init__(self, name, computer, book):  # 将对象 computer 和 book 当作参数来传递
#         self.name = name
#         self.computer = computer
#         # 将书籍信息存放到列表当中
#         self.books = []
#         self.books.append(book)
#
#     def borrow_book(self, book):
#         # 在借书列表中查找
#         for book1 in self.books:
#             if book1.bookname == book.bookname:
#                 print("已经借过此书!")
#                 break
#         else:
#             self.books.append(book)
#             print("借书成功！")
#
#     def show_book(self):
#         for book in self.books:
#             print(book.bookname, end=" ")
#
#     def __str__(self):
#         return self.name + '---' + str(self.computer) + '---' + str(self.books)
#
#
# # 创建对象
# computer = Computer('dell', 'optiplex', '黑色')
#
# book = Book('盗墓笔记', '南派三叔', 10)
#
# stu = Student('yanyan', computer, book)
#
# book2 = Book('鬼吹灯', '天下霸唱', 10)
#
# # 调用方法
# stu.borrow_book(book2)
# stu.show_book()


'''
is a  

base class  父类 基类

继承：
    Student, Employee, Doctor  ---->  都属于人类
    相同代码  -----> 代码冗余，可读性不高
    
    将相同代码提取  ----> Person类
    Student, Employee, Doctor  ----> 继承Person
    
    class Student(Person):
        pass
        
    特点：
    1.如果类中不定义__init__,调用父类 super class的__init__
    2.如果类继承了父类，也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
    3.如果调用父类__init__:
        super().__init__(参数)
        super(类名，对象).__init__(参数)
    4.如果父类有eat(),子类也定义一个eat方法，默认搜索的原则：先找当前类，再去找父类
      s.eat()
      override:重写（覆盖）
      父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    5.子类的方法中也可以调用父类方法：
        super().方法名()
'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(self.name + '正在吃饭...')
#
#     def run(self):
#         print(self.name + '正在跑步...')
#
#
# class Student(Person):
#     def __init__(self, name, age):
#         print("-----init-----")
#         # 如何调用父类__init__
#         super().__init__(name, age)  # super() 父类对象
#
#
# class Employee(Person):
#     pass
#
#
# class Doctor(Person):
#     pass
#
#
# s = Student('yanyan', 18)
# e = Employee('yanyan', 18)
#
# s.run()

# print(s)
# print(e)  # 继承同一个类地址也不同


'''-------------------------------------'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    def __init__(self, name, age, classnumber):
        super(Student, self).__init__(name, age)
        self.classnumber = classnumber

    def study(self, course):
        print('{}正在学习{}'.format(self.name, course))

    def eat(self):
        print("{}喜欢吃嘎嘎".format(self.name))

class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super(Employee, self).__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


student = Student('yanyan', 18, '21研')
employee = Employee('employee', 25, 5000, 'employer')
doctor = Doctor('doctor', 23, ['zhangsan', 'lisi', 'wangwu'])

student.run()
student.eat()
student.study('python')

employee.eat()