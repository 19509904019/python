"""
greenlet已经实现了协程，但是这个工人切换，是不是觉得太麻烦了，不要着急，python还有一个比greenlet更强大的并且能够自动切换任务的模块`gevent`
其原理是当一个greentlet遇到IO（指的是input ouput输入输出，比如网络、文件操作等）操作时，比如访问网络，就自动切换到其他的greenlet,
等到IO完成，再适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent我们自动切换协程，
就保证总有greenlet在运行，而不是等待IO

"""
import time

import gevent
from gevent import monkey

monkey.patch_all()  # 将所有耗时操作进行替换


def task_a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


def task_b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


def task_c():
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(task_a)
    g2 = gevent.spawn(task_b)
    g3 = gevent.spawn(task_c)

    g1.join()
    g2.join()
    g3.join()

    print("--------over!--------")
