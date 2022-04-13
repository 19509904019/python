# 自定义进程
from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 0
        while True:
            print("进程名字：", self.name, "---", n)
            n += 1
            sleep(0.2)


if __name__ == '__main__':
    p = MyProcess('阿燕')
    p.start()
