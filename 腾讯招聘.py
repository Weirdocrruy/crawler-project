#coding = gbk
# -*- coding: UTF-8 -*-
import requests
import time
import os
import sys
import csv
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
fp= open (r'C:\Users\Lenovo-PC\Desktop\腾讯招聘.csv','wt',newline='')
writer = csv.writer(fp)
writer.writerow(('RecruitPostName','CountryName','BGName'))


for page in range(1, 20):
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'
    params = {
        'timestamp': str(time.time()),
        'keyword': 'python',
        'pageIndex': page,
        'pageSize': '10',
        'language': 'zh-cn',
        'area': 'cn'
        }
    response = requests.get(url, params=params).json()
    #print(response)

    data = response["Data"]['Posts']

    # print(data)
    for i in data:
        #print(i)
        RecruitPostName=i['RecruitPostName']
        CountryName=i['CountryName']
        BGName=i['BGName']

         #print("职位名:{RecruitPostName},  国家:{CountryName}".format(**i))
        # print("['RecruitPostName']: ",i['RecruitPostName'])

        writer.writerow((RecruitPostName,CountryName,BGName))
        # work_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # sheet = work_book.add_sheet('test', cell_overwrite_ok=True)
        #
        # # test指表名, cell_overwrite_ok=True允许覆盖写
        # headings = ['职位名', '国家']
        # for i in range(0, len(headings)):
        #     sheet.write(0, i, headings[i])
        #     # 写入第一行 的数据列为len(headings), 每次写入的是第1行第i列的值
        #     work_book.save(r'E:\w11.xls')