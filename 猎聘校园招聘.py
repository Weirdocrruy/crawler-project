# coding=gbk
import requests
from lxml import etree
import csv
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Cookie': '__uuid=1593350604153.65; __tlog=1593350604160.90%7C00000000%7C00000000%7Cs_00_011%7Cs_00_011; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1593350604; __s_bid=5dd497be9dc9b058ac5caadabbf680f3cb10; UniqueKey=152428062e60bd0f1a667e00ad0d9493; access_system=C; user_roles=0; user_photo=5d5513d381fb1a0d6f72bac907u.png; need_bind_tel=false; new_user=true; c_flag=2f709d57abef95eb3ac1a8513ac14b94; gr_user_id=9d724a9b-c4cf-4c07-98ec-c252cb241f52; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id=f5db0b65-a79f-4620-b2cf-38c91a7d0474; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_sid_with_cs1=f5db0b65-a79f-4620-b2cf-38c91a7d0474; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_cs1=152428062e60bd0f1a667e00ad0d9493; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1593350638; grwng_uid=07700cb4-1fe8-4a50-ba93-98faae823a22; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id_f5db0b65-a79f-4620-b2cf-38c91a7d0474=true; _fecdn_=1; Hm_lvt_9bd1bf44f02b38cab5926e780f362426=1593350643; lt_auth=7edcbnIMnA374iXZgDAN4v1I296oUWvM8y5e1hkDh9G%2FWabr4PbjQAOCrLcAxAMhkkx8JMULNLn9Nu3%2Bz3RD7EQSwGmulICyvvuk0H0eTeBnHuyflMXuqs7QQJslrXg6ykpgn2si; JSESSIONID=D678FA3487B55572AF774A32A4A81E89; bad1b2d9162fab1f80dde1897f7a2972_gr_cs1=152428062e60bd0f1a667e00ad0d9493; __session_seq=15; __uv_seq=15; Hm_lpvt_9bd1bf44f02b38cab5926e780f362426=1593351647',
    'DNT': '1',
    'Host': 'campus.liepin.com',
    'Referer': 'https://campus.liepin.com/sojob/search/?keys=%E5%B8%82%E5%9C%BA%E8%90%A5%E9%94%80&dqs=&job_type=&apply_type=&xyjob_jobtitles=&industrys=&e_kind=&sort_type=&folded=1&curPage=2',
}

fp = open(r'C:\Users\Lenovo-PC\Desktop\猎聘校园招聘.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('position', 'company', 'salary', 'city', 'study', 'catagory', 'size', 'desc'))


def get_request(url):
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)
    return html


def get_href():
    html = get_request(url)
    htmls = etree.HTML(html)
    hrefs = htmls.xpath('//p[@class="job-name"]//a/@href')
    # print(hrefs)
    return hrefs


def get_details():
    hrefs = get_href()
    for href in hrefs:
        response = requests.get(href, headers=headers)
        html1 = etree.HTML(response.text)
        position = html1.xpath('//h1[@class="job-name"]/text()')[0]
        company = html1.xpath('//a[@class="company-name"]/text()')[0]
        # company_category = html1.xapth('/html/body/div[2]/aside/div[1]/div[2]/p[3]/text()')[0]
        salary = html1.xpath('//div[@class="job-info"]/span[@class="salary"]/text()')[0]
        city = html1.xpath('//div[@class="job-info"]/span[2]/text()')[0]
        study = html1.xpath('//div[@class="job-info"]/span[3]/text()')[0]
        catagory = html1.xpath('//div[@class="job-info"]/span[4]/text()')[0]
        size = html1.xpath('//div[@class="job-info"]/span[5]/text()')[0]
        desc = re.findall('<p>(.*?)</p>', response.text, re.S)[0]
        print(position, company, salary, city, study, catagory, size, desc)

        writer.writerow((position, company, salary, city, study, catagory, size, desc))


if __name__ == '__main__':
    urls = [
        'https://campus.liepin.com/sojob/search/?keys=%E5%B8%82%E5%9C%BA%E8%90%A5%E9%94%80&dqs=&job_type=&apply_type=&xyjob_jobtitles=&industrys=&e_kind=&sort_type=&folded=1&curPage={}'.format(
            i)
        for i in range(1, 20)]
    for url in urls:
        get_details()
