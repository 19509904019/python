# 进程创建
"""
多进程对于全局变量访问，在每一个全局变量里面都放一个m变量
保证每个进程访问变量互不干扰

m = 1 #可变类型
list1 = []  #不可变类型 
"""
from multiprocessing import Process
from time import sleep

count = 0


def task1():
    global count
    while True:
        sleep(1)
        count += 1
        print("这是任务1....", count)


def task2():
    global count
    while True:
        sleep(2)
        count += 1
        print("这是任务2....", count)


if __name__ == '__main__':
    # 子进程
    p1 = Process(target=task1, name="任务1")
    p1.start()
    p2 = Process(target=task2, name="任务2")
    p2.start()

    print("-" * 50)
