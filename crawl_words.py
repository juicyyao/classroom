from bs4 import BeautifulSoup
import time
import re
import requests
from lxml import etree

def get_word(url_link):
    try:
        req = requests.get(url_link)
        time.sleep(1)
        req.encoding = 'utf=8'
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        result = re.findall(r'P\d*\.doc', html)[0]
        filename = str(soup.title.string)
        tree = etree.HTML(html)
        word_date = tree.xpath('//div/span/text()')[1][3:]
        filename=filename+word_date

        link = url_link.strip('/')
        link = link.split('/')[2:8]
        word_link = '/'.join(link)
        word_link = 'http://' + word_link + '/' + result
        r = requests.get(word_link)
        with open('word/' + filename + '.doc', 'wb')as f:
            f.write(r.content)
    except Exception  as e:
        print (e,word_link,'failed')
try:
    for i in range (17,23):
        if i ==0:
            url='http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj/'
        else:
            url = 'http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj/'+'index_'+str(i)+'.html'

        req = requests.get(url)
        req.encoding = 'utf=8'
        time.sleep(1)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        result = soup.find_all('a', target="_blank")
        url = 'http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj/'
        for link in result:
            link = link.get('href')
            link = link[2:]
            url_link = url + link
            print(url_link)
            get_word(url_link)
except Exception  as e:
    print (e,'failed')

