# coding=gbk
import requests
import you_get
import sys
from lxml import etree
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}


def get_url(url):
    response = requests.get(url, headers=headers).text
    selector = etree.HTML(response)
    # print(selector)
    detail_urls = selector.xpath('//div[@class="content"]/div[@class="info"]/a/@href')
    for detail_url in detail_urls:
        print(detail_url)
        get_Videodownload(detail_url)


def get_Videodownload(detail_url):
    path = './Bվvideo'
    url = detail_url
    sys.argv = ['you-set', '-o', path, url]
    you_get.main()


if __name__ == '__main__':
    url = 'https://www.bilibili.com/ranking/all/3/0/3'
    t = threading.Thread(target=get_url)
    t.start()
    t.join()
    get_url(url)
