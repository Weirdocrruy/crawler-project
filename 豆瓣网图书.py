# coding=gbk
# -*- coding: UTF-8 -*-
from lxml import etree
import requests
import csv

fp = open(r'C:\Users\Lenovo-PC\Desktop\python爬取数据\豆瓣图书.csv', 'wt', newline='',encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))

urls = ['https://book.douban.com/top250?start={}'.format(i)
        for i in range(0, 250, 25)]
# print(urls)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
# print(selector)
for url in urls:
    response = requests.get(url, headers=headers)
    #print(response)
    selector = etree.HTML(response.text)
    #print(selector)
    infos = selector.xpath('//tr[@class="item"]')  # 取大标签
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        print(name)
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else "空"
        writer.writerow((name, url, author, publisher, date, price, rate, comment))

fp.close()
