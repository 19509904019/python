# greenlet 完成协程任务
import time

from greenlet import greenlet


def task_a():
    for i in range(5):
        print('A' + str(i))
        gb.switch()  # 手动切换
        time.sleep(1)


def task_b():
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(1)


def task_c():
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(1)


if __name__ == '__main__':
    ga = greenlet(task_a)
    gb = greenlet(task_b)
    gc = greenlet(task_c)
    print(ga)
    ga.switch()
