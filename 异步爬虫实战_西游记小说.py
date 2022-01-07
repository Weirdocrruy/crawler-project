# coding = gbk
# -*- coding:utf-8 -*-
import requests
import asyncio
import aiohttp
import aiofiles
import json


# https://dushu.baidu.com/api/pc/getCatalog?data={book_id:4306063500}
# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|11348571%22,%22need_bookinfo%22:1}

async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f'{b_id}|{cid}',
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(title, mode='w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])  # 把小说内容写进去


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  # item就是对应每一个章节的名称和cid
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(aiodownload(cid, b_id, title))
    # asyncio.run(asyncio.wait(tasks))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))
