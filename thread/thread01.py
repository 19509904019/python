"""
线程（英语：thread）是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。
在Unix System V及SunOS中也被称为轻量进程（lightweight processes），
但轻量进程更多指内核线程（kernel thread），而把用户线程（user thread）称为线程。

线程自己不拥有系统资源，只拥有一点再运行中必不可少的资源，但它可与同属一个进程的其他线程
共享进程所拥有的全部资源。一个线程可以创建和撤销另一个线程，同一进程中多个线程之间可以并发执行
"""
'''
怎么创建线程？如何使用线程？
    t = threading.Thread(target = func,name ='',args = (1,))
    t.start()
    
线程：
新建  就绪   运行  阻塞  结束


线程是可以共享全局变量的
GIL 全局解释器锁
'''
import threading
from time import sleep

#
#
# # 进程：Process  计算密集型
# # 线程：Thread   耗时操作，爬虫，IO
#
# def download(n):
#     images = ['girl.jpg', 'boy.jpg', 'man.jpg']
#     for image in images:
#         print("正在下载：", image)
#         sleep(n)
#         print(f"下载{image}成功...")
#
#
# def listenMusic():
#     musics = ['last dance', '花海', '迟迟', '清明雨上']
#     for music in musics:
#         sleep(0.4)
#         print(f"正在听{music}...")
#
#
# if __name__ == '__main__':
#     # 线程对象 1s
#     t = threading.Thread(target=download, name='aa', args=(1,))
#     t.start()
#
#     # 0.5s
#     t = threading.Thread(target=listenMusic, name='bb')
#     t.start()

'''------------------------------------------------------------'''

# ticket = 1000
#
#
# def run1():
#     global ticket
#     for i in range(100):
#         ticket -= 1
#
#
# def run2():
#     global ticket
#     for i in range(100):
#         ticket -= 1
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run1, name='1')
#     t2 = threading.Thread(target=run2, name='2')
#
#     t1.start()
#     t2.start()
#
#     print(ticket)


ticket = 0


def run1():
    global ticket
    for i in range(1000000):
        ticket += 1
    print("run1的值为：", ticket)


def run2():
    global ticket
    for i in range(1000000):
        ticket += 1
    print("run2的值为：", ticket)


if __name__ == '__main__':
    t1 = threading.Thread(target=run1, name='1')
    t2 = threading.Thread(target=run2, name='2')

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("现在的值为：", ticket)
