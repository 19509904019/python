"""
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程
但如果时上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待
直到池中有进程结束，才会创建新的进程来执行

阻塞式:添加一个执行一个任务，如果一个任务不结束另一个任务就进不来
非阻塞式:全部添加到队列中立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务完成之后才调用


进程池：
pool = Pool(max)  创建进程池对象
pool.apply()  阻塞式
pool.apply_async() 非阻塞式

pool.close()
pool.join()   给主进程让步
"""
# 非阻塞式
import os
from multiprocessing import Pool
import time
import random


def task(task_name):
    print("开始做任务了...", task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random.random() * 2)
    end = time.time()
    return '完成任务：{}  用时：{}  进程id：{}'.format(task_name, (end - start), os.getpid())


container = []


def callback_func(n):
    """

    :param n: task函数返回的值作为参数
    :return:
    """
    container.append(n)


if __name__ == "__main__":
    pool = Pool(5)

    tasks = ['music', 'game', 'video', 'study', 'cook', 'eat', 'break']
    for i in tasks:
        pool.apply_async(task, args=(i,), callback=callback_func)  # arg参数给task
    pool.close()  # 添加任务结束
    pool.join()

    for c in container:
        print(c)

    print("over!!!")

# # 阻塞式
# import os
# from multiprocessing import Pool
# import time
# import random
#
#
# def task(task_name):
#     print("开始做任务了...", task_name)
#     start = time.time()
#     # 使用sleep
#     time.sleep(random.random() * 2)
#     end = time.time()
#     print('完成任务：{}  用时：{}  进程id：{}'.format(task_name, (end - start), os.getpid()))
#     # return '完成任务：{}  用时：{}  进程id：{}'.format(task_name, (end - start), os.getpid())
#
#
# container = []
#
#
# def callback_func(n):
#     """
#
#     :param n: task函数返回的值作为参数
#     :return:
#     """
#     container.append(n)
#
#
# if __name__ == "__main__":
#     # 进程池容量
#     pool = Pool(5)
#
#     tasks = ['music', 'game', 'video', 'study', 'cook', 'eat', 'relax']
#     for i in tasks:
#         pool.apply(task, args=(i,))  # arg参数给task
#     pool.close()  # 添加任务结束
#     pool.join()
#
#     print("over!!!")
