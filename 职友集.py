# coding=gbk
import requests
from lxml import etree
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
fp = open(r'C:\Users\Lenovo-PC\Desktop\职友集.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('position', 'city', 'work_years', 'position_type', 'salarly', 'education', 'place', 'desc'))


def get_request(url):
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)
    return html


def get_href():
    html = get_request(url)
    htmls = etree.HTML(html)
    hrefs = htmls.xpath('//div[@class="c-job-list"]//div[@class="job-content-box"]//a[@class="job-name"]/@href')
    # for href in hrefs:
    #     detail_url = 'https://www.jobui.com' + href
    #     print(detail_url)
    return hrefs

def get_details():
    hrefs = get_href()
    for href in hrefs:
        detail_url = 'https://www.jobui.com' + href
        print(detail_url)
        response = requests.get(detail_url, headers=headers)
        html1 = etree.HTML(response.text)
        position = html1.xpath('//div[@class="jk-box jk-matter j-job-detail"]/h1/text()')[0]
        city = html1.xpath('//ul[@class="laver cfix fs16"]/li[1]/text()')[0]
        work_years = html1.xpath('//ul[@class="laver cfix fs16"]/li[2]/span[@id="jobAge"]/text()')
        work_years = ''.join(work_years).strip()
        position_type = html1.xpath('//ul[@class="laver cfix fs16"]/li[3]/span[@id="jobType"]/text()')
        position_type = ''.join(position_type).strip()
        salarly = html1.xpath('//ul[@class="laver cfix fs16"]/li[4]/span[@class="fs16 fwb f60"]/text()')
        salarly = ''.join(salarly).strip()
        education = html1.xpath('//ul[@class="laver cfix fs16"]/li[5]/span/text()')
        education  = ''.join(education ).strip()
        place = html1.xpath('//ul[@class="laver cfix fs16"]/li[6]/text()')
        place  = ''.join(place ).strip()
        desc = html1.xpath('//div[@class="cfix"]/div/text()')
        desc = ''.join(desc).strip()
        print(position, city, work_years, position_type, salarly, education, place, desc)
        writer.writerow((position, city, work_years, position_type, salarly, education, place, desc))


if __name__ == '__main__':
    urls = [
        'https://www.jobui.com/jobs?jobKw=%E5%B8%82%E5%9C%BA%E8%90%A5%E9%94%80&cityKw=%E5%85%A8%E5%9B%BD&n={}'.format(i)
        for i in range(1, 10)]
    for url in urls:
        get_details()
