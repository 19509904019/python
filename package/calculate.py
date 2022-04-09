def add(*args):
    if len(args) > 1:
        total = 0
        for i in args:
            total += i
        return total

    else:
        print("至少传入两个参数...")


def minus(*args):
    if len(args) > 1:
        total = 0
        for i in args:
            total -= i
        return total

    else:
        print("至少传入两个参数...")


def multipy(*args):
    if len(args) > 1:
        total = 1
        for i in args:
            total *= i
        return total

    else:
        print("至少传入两个参数...")


def divide(*args):
    pass


class Calculate:
    def __init__(self, num):
        self.num = num

    def test1(self):
        print("----test1----")

    @classmethod
    def test2(cls):
        print("----test2----")
