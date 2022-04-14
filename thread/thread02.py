"""
----------锁----------
共享数据：
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
同步：一个一个的完成，一个做完另一个才能进来，但效率会降低
使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间
多线程的优势在于可以同时运行多个任务（感觉起来这样），但是当线程需要共享数据时，可能存在数据不同步的问题
为了避免这种情况，引入锁的概念

lock = threading.Lock()

lock.acquire()  请求得到锁
....
lock.release()  释放锁

只要不释放其他的线程都无法进入运行状态
"""
import threading
import random
import time

lock = threading.Lock()

list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()


def task2():
    lock.acquire()
    for i in list1:
        print(i)
        time.sleep(0.5)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1, name="1")
    t2 = threading.Thread(target=task2, name="2")

    t2.start()
    t1.start()
    t1.join()
    t2.join()  # 插队，t1 t2 完成后再执行下面语句
    print(list1)
'''
给线程加锁时，只有当一个线程完成后释放锁另一个线程才继续进行，如果不加锁则两个线程会同时并发进行，这样就会对
数据造成错误，但是不考虑线程对数据的影响时，可以用并发线程
'''
