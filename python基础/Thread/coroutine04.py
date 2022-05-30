# 案例


import gevent
from gevent import monkey

monkey.patch_all()

import requests


def download(url):
    response = requests.get(url)
    content = response.text
    print(f'下载了{url}的数据，长度{len(content)}')


if __name__ == '__main__':
    urls = ['https://www.163.com', 'https://www.qq.com', 'https://www.bilibili.com']
    for url in urls:
        gevent.joinall([gevent.spawn(download, url)])
        # gevent.spawn(download, url).join()

    # g1 = gevent.spawn(download, urls[0])
    # g2 = gevent.spawn(download, urls[1])
    # g3 = gevent.spawn(download, urls[2])
    # g1.join()
    # g2.join()
    # g3.join()
    # gevent.joinall([g1, g2, g3])
