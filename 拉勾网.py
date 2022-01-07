# coding=gbk
import requests
import json
import time
import pymongo
import csv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# client = pymongo.MongoClient('localhost', 27017)
# mydb = client['mydb']
# lagou = mydb['lagou']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=3'
}

#
# session=requests.session()
# session.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=3',headers=headers)
# cookies=session.cookies
# cookies.get_dict()
# print(cookies.get_dict())


def get_page(url, params,cookies):
    html = requests.post(url, data=params, headers=headers,cookies=cookies)
    json_data = json.loads(html.text)
    #print(json_data)
    total_count=json_data['content']['positionResult']['totalCount']
    page_number = int(total_count / 15)
    if int(total_count / 15) < 30:
        page_number = int(total_count / 15)
    else:
        page_number = 30
    get_info(url, page_number,cookies)


def get_info(url, page,cookies):
    for pn in range(1, page + 1):
        params = {
            'first': 'true',
            'pn': str(pn),
            'kd': 'python'
        }

        try:
            html = requests.post(url, data=params, headers=headers,cookies=cookies)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos = {
                    #'businessZones': result['businessZones'],
                    'city': result['city'],
                    'companyFullName': result['companyFullName'],
                    #'companyLabelList': result['companyLabelList'],
                    'companySize': result['companySize'],
                    'district': result['district'],
                    'education': result['education'],
                    #'explain': result['explain'],
                    #'firstType': result['firstType'],
                    #'formatCreateTime': result['formatCreateTime'],
                    #'gradeDescription': result['gradeDescription'],
                    #'imState': result['imState'],
                    #'industryField': result['industryField'],
                    #'jobNature': result['jobNature'],
                    #'positionAdvantage': result['positionAdvantage'],
                    'secondType': result['secondType'],
                    'salary': result['salary'],
                    'workYear': result['workYear']
                }
                print(infos)
                #lagou.insert_one(infos)
                time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass


if __name__ == '__main__':
    urls = ['https://www.lagou.com/jobs/list_%E5%B8%82%E5%9C%BA%E8%90%A5%E9%94%80/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput={}'.format(i)for i in range(1, 3)]
    for url in urls:
        session = requests.session()
        session.get(url,headers=headers)
        cookies = session.cookies
        cookies.get_dict()
        url = 'https://www.lagou.com/jobs/positionAjax.json'
        params = {
            'first': 'true',
            'pn': '1',
            'kd': 'python'
        }
        get_page(url, params,cookies)
