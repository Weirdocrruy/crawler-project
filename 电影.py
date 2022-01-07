#coding=gbk
import requests
from multiprocessing import Pool

# urls=['https://youku.com-qq.net/20190626/9408_33b3d9a5/1000k/hls/95b2af046a700000{}.ts'.format(i) for i in range(4, 149)]
# for url in urls:
#     print(url)
#     response=requests.get(url).content
#     with open(r'C:\Users\Lenovo-PC\Desktop\猫眼电影\电影\{}'.format(url[-10:]),'wb') as f:
#         f.write(response)
def download(i):
    url='https://youku.com-qq.net/20190626/9408_33b3d9a5/1000k/hls/95b2af046a7000%03d.ts' % i
    print(url)
    r=requests.get(url)
    ret=r.content
    with open(r'C:\Users\Lenovo-PC\Desktop\猫眼电影\电影\{}'.format(url[-10:]), 'wb') as f:
        f.write(ret)
if __name__=='__main__':
    pool=Pool(20)#进程池
    for i in range(149):
        pool.apply_async(download,args=(i, ))

    pool.close()
    pool.join()
