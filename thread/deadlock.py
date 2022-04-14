"""
开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情

比如说A、B分别是t1和t2的两把锁，当A先占用CPU资源时，此时sleep就进入阻塞状态，然后B占用CPU资源在sleep进入阻塞状态，
当A再次被CPU调用要获取B，但是此时B正处于阻塞状态，当处于就绪状态时CPU正被A占用也进不去，此时就造成了死锁。 互用同一把锁造成了僵持状态

两个或多个线程需要的资源互相被占用，从而一直陷入等待资源被释放

避免死锁，如果出现了：①重构代码  ②在acquire中加timeout

添加timeout时，当等待超时会释放自身的锁
"""

from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class MyThread1(Thread):
    def run(self):  # start
        if lockA.acquire():  # 如果可以获取到锁则返回True
            print(self.name, '获取了A锁')
            time.sleep(0.1)
            if lockB.acquire(timeout=3):  # 此时B锁已经在被使用，阻塞状态
                print(self.name, '获取了B锁,A锁还存在')
                lockB.release()
            lockA.release()


class MyThread2(Thread):
    def run(self):  # start
        if lockB.acquire():  # 如果可以获取到锁则返回True
            print(self.name, '获取了B锁')
            time.sleep(0.1)
            if lockA.acquire():
                print(self.name, '获取了A锁,B锁还存在')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
