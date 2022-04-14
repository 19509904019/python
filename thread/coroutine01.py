"""
协程：微线程  一个进程干多件事情（比如杀毒，正在杀C盘、D盘、E盘、F盘）

进程 > 线程 > 协程

Process   Thread  生成器完成

协程：耗时操作（网络请求   网络下载（爬虫）  IO：文件读写）

"""
import time


def task1():
    for i in range(3):
        print("A" + str(i))
        yield
        time.sleep(1)


def task2():
    for i in range(3):
        print("B" + str(i))
        yield
        time.sleep(1)


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
