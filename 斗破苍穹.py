# coding=gbk
import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
f = open(r'C:\Users\Lenovo-PC\Desktop\斗破苍穹.txt', 'a+')


def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)
        for content in contents:
            f.write(content + '\n')
    else:
        pass


if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(i)
            for i in range(0, 1624)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()
