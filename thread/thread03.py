"""
生产者与消费者：两个线程之间的通信

Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先进先出）队列Queue，LIFO（后进先出）队列LifoQueue，利用先级队列PriorityQueue。
这些队列都实现了锁原语（一般是指由若干条指令组成的程序段，用来实现某个特定功能，在执行过程中不可被中断）
（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用
可以使用队列来实现线程间的同步。

"""
import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put(f"生产者产生数据：{num}")
        print(f"生产者产生数据：{num}")
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"消费者获取到：{item}")
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    tp = threading.Thread(target=produce, args=(q,))
    tp.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    tp.join()
    tc.join()

    print("over!!")

"""
线程：Thread

1.创建线程
    ①  t = threading.Thread(target=func,name='',args=(),kwargs={})  新建状态
        t.start()   -----> 就绪状态
        
        run()
        join()
    
    
    ② 自定义线程
    class MyThread(Thread):
        def __init__(self,name):
            super(MyThread,self).__init()
            self.name = name
                    
        def run(self):
            任务
            
    t = MyThread('name')
    t.start()
    

2.数据共享
   进程共享数据与线程共享数据区别：
    进程是每个进程中都有一份
    线程是同一个数据  ----->  数据安全性问题
    
    GIL ---->  伪线程
    所谓伪线程，就是python中并不是真正的线程，线程在创建过程中并不是加锁的，但是
    python底层会在线程创建时自动加上锁
    
    加锁：
    lock = Lock()
    lock.acquire()
    ....
    lock.release()
    
    
    -----> 可能会产生死锁
    避免死锁

3.线程间通信：生产者与消费者
    生产者：线程
    消费者：线程
    
    q = queue.Queue()   
    
    # 创建生产者
    tp = threading.Thread(target=produce, args=(q,))
    tp.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()
    
    q.put()
    q.get()
    

扩展：GIL
    
"""
