# -*- coding:utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from lxml import etree
def get_pdf(url_link):
    try :
        req = requests.get(url_link)
        req.encoding = 'utf=8'
        time.sleep(1)
        html = req.text
        tree = etree.HTML(html)
        result = tree.xpath('//div[@class="content"]/a/@href')
        filename = tree.xpath('//div[@class="content"]/a/text()')
        filename = ''.join(filename)
        result = ''.join(result)[1:]
        pdf = url_link.strip('/')
        pdf = pdf.split('/')[2:7]
        pdf = 'http://' + '/'.join(pdf) + result
        print(pdf)
        r = requests.get(pdf)
        with open('pdfs/' + filename, 'wb')as f:
            f.write(r.content)
    except:
        print (pdf,'failed')

url = 'http://www.csrc.gov.cn/pub/newsite/fxjgb/yxpl/'
for i in range (22,41):
    try:
        if i== 0:
            url = 'http://www.csrc.gov.cn/pub/newsite/fxjgb/yxpl/'
        else:
            url = url + 'index_' + str(i) + '.htm'
        req = requests.get(url)
        req.encoding = 'utf=8'
        time.sleep(1)
        html=req.text
        soup=BeautifulSoup(html,'lxml')
        result=soup.find_all('a',target="_blank")
        url = 'http://www.csrc.gov.cn/pub/newsite/fxjgb/yxpl/'
        for link in result:
            link=link.get('href')
            link=link[9:]
            url_link='http://www.csrc.gov.cn/pub/'+link
            print (url_link)
            get_pdf(url_link)
    except:
        print (url_link,'failed')