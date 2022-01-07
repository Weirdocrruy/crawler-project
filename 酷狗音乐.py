# coding=gbk
import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}


fp = open(r'C:\Users\Lenovo-PC\Desktop\酷狗音乐.csv', 'wt', newline='', encoding='UTF-8-sig')
writer = csv.writer(fp)
writer.writerow(('rank', 'singer', 'song', 'time'))


def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    # rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > span.pc_temp_num > strong
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    # rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > a
    times = soup.select('span.pc_temp_tips_r > span')
    # rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > span.pc_temp_tips_r > span
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0],
            'song': title.get_text().split('-')[1],
            'time': time.get_text().strip()

        }
        #print(data)

        rank=data['rank']
        singer=data['singer']
        song=data['song']
        time=data['time']


        writer.writerow((rank, singer, song, time))
if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(i) for i in range(1, 24)]
    for url in urls:
        get_info(url)
        time.sleep(1)
