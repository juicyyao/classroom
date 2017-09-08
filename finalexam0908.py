import requests
from lxml import etree
import urllib.request
from threading import Thread
home_page=int(input('input the home page:'))
termination_page=int(input('input the termination page:'))
def down_pic(url):
    filename = link.split('/')[-1]
    try:
        link='http:'+link
        with open(filename,'wb') as file:
            file.write(link.content)
        #urllib.request.urlretrieve('http:' + link, 'pics/' + filename)
        print(filename, '#####success#####')
    except:
        print(filename, '#####failed#####')
for page in range(home_page,termination_page+1):
    url='http://jiandan.net/pic/page-%d'% page
    print('====', 'downloading', url, '====')
    req=requests.get(url)
    content=req.text
    content1=etree.HTML(content)
    content2=content1.xpath('//a[@class="view_img_link"]/@href')
    for link in content2:
        t=Thread(target=down_pic,args=(link,))
        t.start()
        down_pic(link)


