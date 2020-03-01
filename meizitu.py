import requests
from bs4 import BeautifulSoup
import bs4
import os
import time
import re

head = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
        'Connection': 'Keep-Alive',
        'Referer': "http://www.mzitu.com/99566"}

print('********************************************************')
print('*                                                      *')
print('*      欢迎使用《小强三号v2.0测试版》（单线程）        *')
print('*                                                      *')
print('* 因为此程序是在此文件根目录运行的，所以最好在桌面新建 *')
print('*   一个文件夹，把此文件放进去再运行，以保护文件系统   *')
print('********************************************************')
print()
print('请输入需要开始查看的年份（2013、2014、2015…2020）并按回')
print('车键继续，输入其他内容则从2016年开始')

m = 56141
o = input()
if int(o) == 2013:
    m = 1
if int(o) == 2014:
    m = 19449
if int(o) == 2015:
    m = 34533
if int(o) == 2016:
    m = 56141
if int(o) == 2017:
    m = 82890
if int(o) == 2018:
    m = 114353
if int(o) == 2019:
    m = 164018
if int(o) == 2020:
    m = 202827
url = "https://www.mzitu.com/" + str(m)

def getHTMLText(url):
    try:
        q = requests.get(url,headers = head,timeout = 20)
        q.raise_for_status()
        q.encoding = q.apparent_encoding
        return q.text
    except:
        return ""

def downPic(text,pathNam):
    soup = BeautifulSoup(text,"html.parser")
    soupl = soup.find('div','main-image').find('a')
    for src in soupl:
        if isinstance(src,bs4.element.Tag):
            tu = src.get('src')
    sp = tu.split('/')[-1]
    if not os.path.exists('./' + pathName):
        os.mkdir('./' + pathName)
    rPath = './' + pathName + '/' + sp
    with open(rPath,'wb') as f:
        q1 = requests.get(tu,headers = head,timeout = 20)
        f.write(q1.content)
        f.close()

def Next(text):
    try:
        soup = BeautifulSoup(text,"html.parser").find('div','main-image').find('a')
        nextPage = soup.get('href')
        return nextPage
    except:
        return ""

while 1:
    try:
        TEXT = getHTMLText(url)
        time.sleep(0.26)
        pathName = re.search(r'[\u4E00-\u9FA5a-zA-Z0-9]+',BeautifulSoup(TEXT,"html.parser").find('title').string).group(0)
        downPic(TEXT,pathName)
        os.system('cls')
        print('魔法施放中：' + pathName)
        time.sleep(0.26)
        url = Next(TEXT)
    except:
        continue

