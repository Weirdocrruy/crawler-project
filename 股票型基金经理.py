# coding=gbk
import requests
from lxml import etree
import csv
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
fp = open(r'C:\Users\Lenovo-PC\Desktop\好买网基金经理完整.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('基金规模','成立时间','经验值', '绩效点', '风控能力', '稳定性', '跳槽频率', '基金数', '历任公司数', '人气指数', '近三月回报率', '从业年数', '年均回报率',
                 '1年内夏普比率', '2年内夏普比率', '类型', '经理名字'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': '__hutmmobile=929AB775-A85A-4B7F-BAD5-7C6D7B7448E8; _ga=GA1.2.1416576763.1617259713; _gid=GA1.2.612451186.1618886455; _zero_hbtrack=0.2800000; __hutmc=268394641; __hutmz=268394641.1618895711.8.3.hutmcsr=baidu|hutmccn=(organic)|hutmcmd=organic; _hbotrack=2800000-0-0-0.0; _hb_ref_pgid=11010; SESSION=9c0dd13e-3dd0-49ed-b490-ab0f0f840e8b; _hb_pgid=; Hm_lvt_394e04be1e3004f9ae789345b827e8e2=1618886455,1618887491,1618895711,1618896167; GM_VISIT_COOKIE=007130%2C161718%2C004040; __hutma=268394641.717726182.1617259712.1618895711.1618904597.9; OZ_SI_1497=sTime=1618895711&sIndex=28; OZ_1U_1497=vid=v0656cc0f164e0.0&ctime=1618904636&ltime=1618904596; OZ_1Y_1497=erefer=https%3A//www.baidu.com/link%3Furl%3Df5_CSNPoiRT43_nOHnY5rCccmo-UMTSI_TLZItMTP8vdi_3KE9VJUxof5F-vxU0g%26ck%3D7949.1.72.434.150.432.158.438%26shh%3Dwww.baidu.com%26sht%3D88093251_22_hao_pg%26wd%3D%26eqid%3Dd1abc56a00018e4100000006607e651f%26tn%3D88093251_22_hao_pg&eurl=https%3A//www.howbuy.com/fund/161718/&etime=1618896166&ctime=1618904636&ltime=1618904596&compid=1497; __hutmb=268394641.2.10.1618904597; Hm_lpvt_394e04be1e3004f9ae789345b827e8e2=1618904637'
}

url = 'https://www.howbuy.com/fund/manager/ajax.htm'
for page in range(1, 150):
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
    res = requests.post(url, headers=headers, data=data)
    response = json.loads(res.text)
    rydms = response['list']
    for rydm1 in rydms:
        rydm = 'https://www.howbuy.com/fund/manager/' + rydm1['rydm'] + '/'
        response1 = requests.get(rydm, headers=headers)
        # print(response1.text)
        html = etree.HTML(response1.text)
        indexs = html.xpath('//div[@class="manager_pub_title"]/div[@class="manager_title"]/span/text()')
        detail = []
        if len(indexs) != 0:
            Empirical_values = indexs[0]
            Fighting_capacitys = indexs[1]
            Defensivenesss = indexs[2]
            Stabilitys = indexs[3]
            #likes = indexs[4]
            detail.append(Empirical_values)
            detail.append(Fighting_capacitys)
            detail.append(Defensivenesss)
            detail.append((Stabilitys))
            #detail.append(likes)

        Job_hoppingss = html.xpath('//div[@class="content_m fl"]/table/tr[2]/td[4]/text()')
        yearss = html.xpath('//div[@class="content_m fl"]/table/tr[1]/td[4]/text()')
        # print(yearss)
        Average_annualss = html.xpath('//div[@class="content_m fl"]/table/tr/td/span[@class="cRed"]/text()')
        Popularityss = html.xpath('//div[@class="manager_info_right fl"]/ul/li[5]/span/text()')
        typess = html.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[3]/span/text()')
        managerss = html.xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div/text()')
        numberss = html.xpath('//*[@id="lsgljj_0"]/div[1]/span/text()')
        companyss = html.xpath('//div[@class="content_m fl"]/table//tr[2]/td[2]/text()')
        rewardss = html.xpath('//*[@id="experience"]/div[3]/div[3]/div[3]/ul/li[2]/span/text()')
        # stdss = html.xpath('//*[@id="stability"]/div[3]/div[3]/div[3]/ul/li[1]/span/text()')
        reprent = html.xpath('//div[@class="manager_info_right fl"]/ul/li[4]/a/@href')
        # print(reprent)
        if len(reprent) != 0:
            response2 = requests.get(reprent[0], headers=headers)
            html1 = etree.HTML(response2.text)
            sharp_1ss = html1.xpath('//*[@id="nTab2_0"]/div[5]/div[2]/div[2]/div/div[3]/table/tbody/tr[3]/td[2]/text()')
            sharp_2ss = html1.xpath('//*[@id="nTab2_0"]/div[5]/div[2]/div[2]/div/div[3]/table/tbody/tr[3]/td[3]/text()')
            sizess = html1.xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/ul/li[3]/span/text()')
            timess = html1.xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/ul/li[4]/span/text()')
            # print(sharp_1ss, sharp_2ss)
        if len(Job_hoppingss) != 0:
            Job_hoppings = Job_hoppingss
            Job_hoppings = ''.join(Job_hoppingss).strip()
            Average_annuals = Average_annualss
            Average_annuals = ''.join(Average_annualss).strip()
            Popularitys = Popularityss
            Popularitys = ''.join(Popularityss).strip()
            types = ''.join(typess).strip()
            years = ''.join(yearss).strip()
            managers = ''.join(managerss).strip()
            numbers = ''.join(numberss).strip()
            companys = ''.join(companyss).strip()
            rewards = ''.join(rewardss).strip()
            # stds = ''.join(stdss).strip()
            sharp_1s = ''.join(sharp_1ss).strip()
            sharp_2s = ''.join(sharp_2ss).strip()
            sizes = ''.join(sizess).strip()
            times = ''.join(timess).strip()
            detail.append(Job_hoppings)
            detail.append(Popularitys)
            detail.append((Average_annuals))
            detail.append(types)
            detail.append(years)
            detail.append(managers)
            detail.append(numbers)
            detail.append(companys)
            detail.append(rewards)
            # detail.append(stds)
            detail.append(sharp_1s)
            detail.append(sharp_2s)
            detail.append(sizes)
            detail.append(times)

        # print(detail)
        if len(detail) != 0:
            Empirical_value = detail[0]
            Fighting_capacity = detail[1]
            Defensiveness = detail[2]
            Stability = detail[3]
            #like = detail[4]
            Job_hopping = detail[4]
            Popularity = detail[5]
            Average_annual = detail[6]
            type = detail[7]
            year = detail[8]
            # std = detail[9]
            manager = detail[9]
            number = detail[10]
            company = detail[11]
            reward = detail[12]
            sharp_1 = detail[13]
            sharp_2 = detail[14]
            size = detail[15]
            time = detail[16]
            writer.writerow(
                (size,time,Empirical_value, Fighting_capacity, Defensiveness, Stability, Job_hopping, number, company,
                 Popularity, reward, year, Average_annual, sharp_1, sharp_2, type, manager))
            print(size,time,Empirical_value, Fighting_capacity, Defensiveness, Stability, Job_hopping, number, company,
                  Popularity, reward, year, Average_annual, sharp_1, sharp_2, type, manager)
