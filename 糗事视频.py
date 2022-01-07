# coding=gbk
import os
from threading import Thread
from queue import Queue
import requests
from bs4 import BeautifulSoup
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


# ��дһ��������
class CrawInfo(Thread):
    # ��д���췽��
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        # ����������
        self.url_queue = url_queue
        self.html_queue = html_queue

        # ������Ƶ�洢�ļ���
        if not os.path.exists('./������Ƶ/'):
            os.mkdir('./������Ƶ/')

        # ��д���߳��е������̵߳ĺ���
        def run(self):
            while not self.url_queue.empty():
                url = self.url_queue.get()
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    self.html_queue.put(response.text)


class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while not self.html_queue.empty():
            soup = BeautifulSoup(self.html_queue.get(), 'lxml')
            videos_data = soup.find_all('source')
            for video in videos_data:
                video_url = video['src']
                with open('./������Ƶ/' + os.path.split(video_url)[0][31:] + os.path.split(video_url)[-1],
                          'wb') as f:
                    data = requests.get('https:' + video_url, headers=headers).content
                    f.write(data)
                    print('������ɣ�' + os.path.split(video_url)[0][31:])


if __name__ == '__main__':
    url_queue = Queue()
    html_queue = Queue()

    base_url = 'https://www.qiushibaike.com/video/page/{}/'
    for page in range(1, 14):
        new_url = base_url.format(page)

    # �����߳���������
    crawl_list = []
    for x in range(3):
        crawl = CrawInfo(url_queue, html_queue)
        crawl_list.append(crawl)
        crawl.start()

    # ��Ҫ���̶߳������join�������ȴ������߳�������ɺ����˳�
    for _ in crawl_list:
        _.join()

    parse_list = []
    for x in range(3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()

    for _ in parse_list:
        _.join()
