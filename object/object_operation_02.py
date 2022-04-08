"""
私有化

封装：1.私有化属性   2.定义共有set和get方法
__属性：就是将属性私有化，访问范围仅仅限于类中

好处：
1.隐藏属性不被外界随意修改
2.也可以修改：通过函数(在函数内可以筛选赋值的内容)
    def setXXX(self,XXX):
        if xxx是否符合条件
            赋值
        else:
            不赋值

3.如果想获取具体的而某一个属性
使用get函数
    def getXXX(self):
        return self.__xxx
"""


# class Student:
#     # __age = 18  # 类属性
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#         self.__score = 59
#
#     # 定义公有set和get方法
#     # set是为了赋值
#     def setAge(self, age):
#         if 0 < age < 100:
#             self.__age = age
#         else:
#             print("年龄不符合！")
#
#     # get是为了取值
#     def getAge(self):
#         return self.__age
#
#
#     def __str__(self):
#         return '姓名：{}，年龄：{}，考试分数：{}'.format(self.name, self.__age, self.__score)


# yanyan = Student('yanyan', 18)
# yanyan.__age = 20  # 私有化属性无法修改
# print(yanyan)


# yanyan.setAge(20)
# print(yanyan)

# print(yanyan.getAge())

# print(dir(Student))
# print(dir(yanyan))

# print(yanyan.__age)  #_Student__age
# print(yanyan._Student__age)  # 其实它就是__age,只不过系统自动改名字了
# print(yanyan.__dir__())  # 同print(dir(对象名))


# 在开发中看到一些私有化处理：装饰器

class Student:
    # __age = 18  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__score = 100

    # # 定义公有set和get方法
    # # set是为了赋值
    # def setAge(self, age):
    #     if 0 < age < 100:
    #         self.__age = age
    #     else:
    #         print("年龄不符合！")
    #
    # # get是为了取值
    # def getAge(self):
    #     return self.__age
    #     # return self.__score

    # 现有getxxx
    @property
    def age(self):
        return self.__age

    # 再有set,因为set依赖get
    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("年龄不符合！")

    def __str__(self):
        return '姓名：{}，年龄：{}，考试分数：{}'.format(self.name, self.__age, self.__score)


yanyan = Student("yanyan", 18)
yanyan.name = 'ayan'
print(yanyan)

# 私有化赋值
# yanyan.setAge(20)
# print(yanyan.getAge())

# print(yanyan.age)

yanyan.age = 10000
print(yanyan.age)
