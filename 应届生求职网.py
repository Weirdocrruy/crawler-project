# coding=gbk
import requests
from lxml import etree
import csv
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

fp = open(r'C:\Users\Lenovo-PC\Desktop\应届生求职网.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('updata', 'city', 'job_type', 'resouce', 'position', 'desc'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


def get_request(url):
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)
    return html


def get_href():
    html = get_request(url)
    htmls = etree.HTML(html)
    hrefs = htmls.xpath('//div/h3[@class="title"]/a/@href')
    return hrefs


def get_details():
    hrefs = get_href()
    for href in hrefs:
        print(href)
        response = requests.get(href, headers=headers)
        response.encoding = 'gbk'
        html = etree.HTML(response.text)
        updata = html.xpath('//div[@class="info clearfix"]//li[1]/u/text()')
        updata = ''.join(updata).strip()
        city = html.xpath('//div[@class="info clearfix"]//li[2]/u/text()')
        city = ''.join(city).strip()
        job_type = html.xpath('//div[@class="info clearfix"]//li[3]/u/text()')
        job_type = ''.join(job_type).strip()
        resouce = html.xpath('//div[@class="info clearfix"]//li[4]/a/text()')
        resouce = ''.join(resouce).strip()
        position = html.xpath('//div[@class="info clearfix"]//li[5]/u/text()')
        position = ''.join(position).strip()
        print(updata, city, job_type, resouce, position)

        desc = re.findall('<p>(.*?)</p>', response.text, re.S)
        desc = ''.join(re.findall(u'[0-9\u4e00-\u9fa5]+', str(desc), re.S)).strip()
        if desc == 0:
            desc = re.findall(
                '<p style="margin: 0px; padding: 0px; font-family: sans-serif; font-size: 16px; text-indent: 2em; background: none !important;">(.*?)</p>',
                response.text, re.S)
            desc = ''.join(re.findall(u'[0-9\u4e00-\u9fa5]+', str(desc), re.S)).strip()
            print(desc)
        else:
            desc = re.findall('<p>(.*?)</p>', response.text, re.S)
            desc = ''.join(re.findall(u'[0-9\u4e00-\u9fa5]+', str(desc), re.S)).strip()
            print(desc)
        writer.writerow((updata, city, job_type, resouce, position, desc))


if __name__ == '__main__':
    urls = [
        'https://s.yingjiesheng.com/search.php?word=%E5%B8%82%E5%9C%BA%E8%90%A5%E9%94%80&sort=score&start={}'.format(i)
        for i in range(0, 200, 10)]
    for url in urls:
        get_details()
