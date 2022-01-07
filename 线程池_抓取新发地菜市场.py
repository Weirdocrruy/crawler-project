# coding = gbk
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open('data.csv', mode='w', encoding='utf-8')
csvwriter = csv.writer(f)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


def domnload_one_page(url):
    resp = requests.get(url, headers=headers)
    # resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    table = html.xpath('/html/body/div[2]/div[4]/div[1]/table')[0]
    # trs = table.xpath('./tr')[1:]
    trs = table.xpath('./tr[position()>1]')
    for tr in trs:
        txt = tr.xpath('./td/text()')
        txt = (item.replace('\\', '').replace('/', '') for item in txt)
        csvwriter.writerow(txt)
    print(url, '下载完毕！')


if __name__ == '__main__':
    # for i in range(1,14870):  # 效率低
    #     domnload_one_page(f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    #  创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            # 把下载任务提交给线程池
            t.submit(domnload_one_page, f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    print('全部下载完毕！')
