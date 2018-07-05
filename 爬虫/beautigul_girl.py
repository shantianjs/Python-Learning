import requests
from bs4 import BeautifulSoup
import chardet
import re
import os
import multiprocessing
import time
import lxml
import random

#设置请求头
def header(referer):
    headers={
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

#获取页面链接
def getPage(pageNum):
    baseURL = 'http://www.mzitu.com/page/{}/'.format(pageNum)
    html = requests.get(baseURL).content.decode('utf-8')
    bf = BeautifulSoup(html,'lxml')
    ul = bf.find(name='ul',id='pins')
    urls = []
    for i in ul.contents:
        try:
            urls.append(i.find_all('a')[0].get('href'))
        except:
            continue
    # pattern = re.compile(r'href="(http:\/\/www.mzitu.com\/\d*)"') #使用正则
    # for i in ul.contents:
    #     url=pattern.search(str(i))
    #     if not url:
    #         continue
    #     print(url.group(1))
    #     urls.append(url)
    print('获取连接{}'.format(len(urls)))
    l = len(urls)
    return  urls

def getPicture(url):
    sel = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(sel,'lxml')
    # 标题
    title = soup.find('div', attrs={'class': 'main-image'}).p.a.next.get('alt')
    #当前总图片数
    navi = soup.find('div',attrs={'class':'pagenavi'})
    links = navi.find_all('a')
    pattern = re.compile('\d*$')
    searched = pattern.search(links[-2].get('href'))
    if searched:
        total = int(searched.group())
    else:
        raise IOError('url is error')

    #建立文件夹
    dirname = f'【{ total }P】{ title }'
    try:
        os.mkdir(dirname)
    except:
        # print(f"{dirname}  已存在")
        pass
    for i in range(1,2):#total+1
        link = f'{url}/{i}'
        soup = BeautifulSoup(requests.get(link).content.decode('utf-8'),'lxml')
        #对于每一页
        filename = r"{}\{}\{}.jpg".format(os.path.abspath('.'),dirname,i)
        print(f'开始下载{dirname}第{i}张{os.getpid()}')
        try:
            with open(filename,'wb') as jpg:
                # 当前页图片链接
                picture = soup.find('div', attrs={'class': 'main-image'}).p.a.next.get('src')
                try:
                    jpg.write(requests.get(picture,headers=header(f'{url}/{i}')).content)
                except:
                    print(f"{filename}没有下载成功")
        except:
            print(filename)
            break

    return dirname


if __name__== '__main__':
    for pageNum in range(3,4):
        urls = getPage(pageNum)
        print(urls)
        pool = multiprocessing.Pool(processes=4)
        #pool.map(getPicture,urls)
        for url in urls:
            pool.apply_async(getPicture,args=(url,))
         #默认开启，先关闭进程池
        pool.close()
        print('pool strat')
        pool.join()
        print('pool end')
        time.sleep(random.choice([x for x in range(5, 10)]))




