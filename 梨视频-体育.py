import re
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

response = requests.get('https://www.pearvideo.com/category_9')
html = response.text
# print(html)
mp4_url = re.findall('href="(.*?)"', html)
mp4_url.sort()
nums = mp4_url[-10:-1]
for num in nums:
    i = re.sub('video_', '', num)
    # print(i)
    urls = 'https://www.pearvideo.com/video_{}'.format(i)
    # print(urls)

    response = requests.get(urls)
    html = response.text
    # print(html)
    mp4_url = re.findall('srcUrl="(.*?)"', response.text)
    name = re.findall('<h1 class="Bվvideo-tt">(.*?)</h1>', response.text, re.S)
    mp4 = mp4_url[0]
    # print(mp4)
    # print(name)

    response = requests.get(mp4)

    f = open("{}.mp4".format(name), mode='wb')
    f.write(response.content)
    f.close()
