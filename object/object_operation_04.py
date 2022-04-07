class Base:
    def test(self):
        print("------> Base")


class A(Base):
    def test(self):
        print("----->AAAA")


class B(Base):
    def test(self):
        print("----->BBBB")


class C(Base):
    def test(self):
        print("----->CCCC")


class D(A, B, C):
    pass


d = D()
d.test()

'''
python 允许多继承

def 子类（父类1,父类2,...）:
    pass

多继承的搜索顺序：经典类  新式类
'''


# 经典类  搜索规则：深度优先
# class P1:
#     def foo(self):
#         print("p1 ---> foo")
#
#     def bar(self):
#         print("p1 ---> bar")
#
#
# class P2:
#     def foo(self):
#         print("p2 ---> foo")
#
#
# class C1(P1, P2):
#     pass
#
#
# class C2(P1, P2):
#     def bar(self):
#         print("C2 ---> bar")
#
#
# class D(C1, C2):
#     pass
#
#
# print(D.__mro__)  #查看搜索顺序
# d = D()
# d.foo()
# d.bar()


# 新式类   广度优先
class P1(object):
    def foo(self):
        print("p1 ---> foo")

    def bar(self):
        print("p1 ---> bar")


class P2(object):
    def foo(self):
        print("p2 ---> foo")


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print("C2 ---> bar")


class D(C1, C2):
    pass


print(D.__mro__)
d = D()
d.foo()
d.bar()

"""
多态  封装  继承  ---->  面向对象
"""


class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可以接收cat,也可以接收dog,还可以接收tiger  多态
        if isinstance(pet, Pet):
            print("{}喜欢养宠物：{},昵称是：{}".format(self.name, cat.role, cat.nickname))
        else:
            print("不是宠物类型的...")


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print("昵称：{}，年龄：{}".format(self.nickname, self.age))


class Cat(Pet):
    role = 'Cat'

    def catch_mouse(self):
        print("抓老鼠...")


class Dog(Pet):
    role = 'Dog'

    def watch_house(self):
        print("看家高手...")


class Tiger:
    def show(self):
        print("太可怕了，会吃人...")


# 创建对象
cat = Cat("huahua", 2)

dog = Dog("xiaohei", 4)

tiger = Tiger()
person = Person("家伟")

person.feed_pet(cat)
person.feed_pet(tiger)
