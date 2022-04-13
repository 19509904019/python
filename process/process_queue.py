"""
进程间的通信

"""
from multiprocessing import Queue
from time import sleep

# # 队列
# q = Queue(5)
# list1 = ['1', '2', '3', '4', '5']
# for i in list1:
#     q.put(i)
#
# if not q.full():  # 判断队列是否满    q.empty() 判断队列是否为空
#     q.put('6')  # put()如果queue满了则只能等待，当有空位才会添加成功
#
# else:
#     print("队列已满！")
# #
# for i in range(6):
#     # print(q.get())
#     # print(q.get(timeout=3))
#     print(q.get_nowait())

"""
put_nowait()
get_nowait()
"""
from multiprocessing import Process


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print("正在下载：", image)
        sleep(0.5)
        q.put(image, timeout=1)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=2)
            print(f"{file}保存成功！")
        except:
            print("全部保存完毕！")
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
