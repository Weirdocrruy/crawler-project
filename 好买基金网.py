# coding = gbk
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests
import json
from lxml import etree
import csv

f = open("data.csv", mode="w", newline='', encoding='utf-8-sig')
csvwriter = csv.writer(f)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': '__hutmmobile=929AB775-A85A-4B7F-BAD5-7C6D7B7448E8; _ga=GA1.2.1416576763.1617259713; _gid=GA1.2.612451186.1618886455; '
              '_zero_hbtrack=0.2800000; __hutmc=268394641; __hutmz=268394641.1618895711.8.3.hutmcsr=baidu|hutmccn=(organic)|hutmcmd=organic; '
              '_hbotrack=2800000-0-0-0.0; _hb_ref_pgid=11010; SESSION=9c0dd13e-3dd0-49ed-b490-ab0f0f840e8b; '
              '_hb_pgid=; Hm_lvt_394e04be1e3004f9ae789345b827e8e2=1618886455,1618887491,1618895711,1618896167; '
              'GM_VISIT_COOKIE=007130%2C161718%2C004040; __hutma=268394641.717726182.1617259712.1618895711.1618904597.9; '
              'OZ_SI_1497=sTime=1618895711&sIndex=28; OZ_1U_1497=vid=v0656cc0f164e0.0&ctime=1618904636&ltime=1618904596; '
              'OZ_1Y_1497=erefer=https%3A//www.baidu.com/link%3Furl%3Df5_CSNPoiRT43_nOHnY5rCccmo-UMTSI_TLZItMTP8vdi_'
              '3KE9VJUxof5F-vxU0g%26ck%3D7949.1.72.434.150.432.158.438%26shh%3Dwww.baidu.com%26sht%3D88093251_22_hao_'
              'pg%26wd%3D%26eqid%3Dd1abc56a00018e4100000006607e651f%26tn%3D88093251_22'
              '_hao_pg&eurl=https%3A//www.howbuy.com/fund/161718/&etime=1618896166&ctime=1618904636&ltime=1618904596&compid=1497; __'
              'hutmb=268394641.2.10.1618904597; Hm_lpvt_394e04be1e3004f9ae789345b827e8e2=1618904637'
}


def get_detail_url(url, data):
    detail_urls = []
    res = requests.post(url, headers=headers, data=data)
    response = json.loads(res.text)
    # print(response)
    rydms = response['list']
    for rydm1 in rydms:
        rydm = 'https://www.howbuy.com/fund/manager/' + rydm1['rydm'] + '/'
        detail_urls.append(rydm)
    return detail_urls


def get_detail(rydm):
    response = requests.get(rydm, headers=headers)
    # print(response.text)
    html = etree.HTML(response.text)
    details = []
    try:
        popurity = html.xpath('//div[@class="manager_info_right fl"]/ul/li[5]/span/text()')[0].strip()
        time = html.xpath('//div[@class="content_m fl"]/table/tr[1]/td[4]/text()')[0].strip()
        defense = html.xpath('//*[@id="defense"]/div[1]/div/span/text()')[0].strip()
        stably = html.xpath('//*[@id="stability"]/div[1]/div/span/text()')[0].strip()
        jop = html.xpath('//div[@class="content_m fl"]/table/tr[2]/td[4]/text()')[0].strip()
        number = html.xpath('//*[@id="dqgljj_0"]/div[2]/div[1]/span/text()')[0].strip()
        type = html.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[3]/span/text()')[0].strip()
        reprent_url = html.xpath('//div[@class="manager_info_right fl"]/ul/li[4]/a/@href')[0].strip()
        print(popurity, time, defense, stably, jop, number, type, reprent_url)
        details.append(popurity)
        details.append(time)
        details.append(defense)
        details.append(stably)
        details.append(jop)
        details.append(number)
        details.append(type)
        details.append(reprent_url)

    except IndexError:
        pass
    return details


def get_reprent_url(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    details = []
    try:
        size = html.xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/ul/li[3]/span/text()')[0].strip()
        open = html.xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/ul/li[4]/span/text()')[0].strip()
        sharpe = html.xpath('//*[@id="nTab2_0"]/div[5]/div[2]/div[2]/div/div[3]/table/tbody/tr[3]/td[3]/text()')[
            0].strip()
        # print(size, open, sharpe)
        details.append(size)
        details.append(open)
        details.append(sharpe)

    except IndexError:
        pass
    return details


def main(url, data):
    urls = get_detail_url(url, data)
    for detail_url in urls:
        details = get_detail(detail_url)
        if len(details) != 0:
            detail_1 = get_reprent_url(details[7])
            detail_2 = details[:-1]
            most_details = detail_1 + detail_2
            csvwriter.writerow(most_details)


if __name__ == '__main__':
    url = 'https://www.howbuy.com/fund/manager/ajax.htm'
    for page in range(1, 100):
        data = {
            'wzfl': '',
            'cynx': '',
            'jgdm': '',
            'keyword': '',
            'ryzt': '',
            'orderField': 'rqzs',
            'orderType': 'true',
            'page': page
        }
        main(url, data)
