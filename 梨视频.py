# coding=gbk
import requests
import re
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

response = requests.get('https://www.pearvideo.com/video_1651895')
html = response.text
#print(html)
mp4_url = re.findall('srcUrl="(.*?)"', response.text)
name = re.findall('<h1 class="Bվvideo-tt">(.*?)</h1>', response.text,re.S)
print(mp4_url)
print(name)

response = requests.get('https://video.pearvideo.com/mp4/adshort/20200213/cont-1651895-14906491_adpkg-ad_hd.mp4')

f = open("{}.mp4".format(name), mode='wb')
f.write(response.content)
f.close()