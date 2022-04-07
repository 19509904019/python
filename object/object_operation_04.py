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
