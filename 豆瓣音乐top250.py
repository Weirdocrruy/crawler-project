# coding=gbk
import requests
from lxml import etree
import re
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
musictop = mydb['musictop']
# url='https://music.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}


def get_url_music(url):
    html = requests.get(url, headers=headers)
    # print(html)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//a[@class="nbg"]/@href')
    for music_href in music_hrefs:
        # print(music_href)
        get_music_info(music_href)


def get_music_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    author = selector.xpath('//*[@id="info"]/span[1]/span/a/text()')
    styles = re.findall('<span class="p1">����:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(styles) == 0:
        style = 'δ֪'
    else:
        style = styles[0].strip()
    time = re.findall('����ʱ��:</span>&nbsp;(.*?)<br />', html.text, re.S)[0].strip()
    publishers = re.findall('������:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(publishers) == 0:
        publisher = 'δ֪'
    else:
        publisher = publishers[0].strip()
    score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    print(name, author, style, time, publisher, score)
    info = {
        'name': name,
        'author': author,
        'style': style,
        'time': time,
        'publisher': publisher,
        'score': score
    }
    musictop.insert_one(info)


if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(i) for i in range(0, 50, 25)]
    for url in urls:
        get_url_music(url)
        time.sleep(2)
