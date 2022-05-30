"""

循环导入：大型的python项目中，需要很多python文件，由于架构不当，可能会出现模块之间的相互导入
    A:
        def test():
            f()

    B:
        def f():
            test()


解决办法：
1.重新架构
2.把导入语句放到模块的最后
3.将导入的语句放到函数里面
"""
from circular_import1 import func


def task1():
    print("-----task1-----")


def task2():
    print("-----task2-----")
    func()


if __name__ == '__main__':

    task1()
    task2()
