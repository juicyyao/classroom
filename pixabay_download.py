import requests
from bs4 import BeautifulSoup
from threading import Thread

header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

def download_pic (link):
    print ('downloading',link)
    filename = link.split('/')[-1]
    retries = 0
    while retries < 3:
        try:
            pic = requests.get(link)
            with open('pic/' + filename, 'wb') as f:
                f.write(pic.content)
        except:
            retries +=1
            print(filename,'failed')
        else:
            print (filename,'saved')
            break
url='https://pixabay.com/'
req=requests.get(url,headers=header)
html=req.text
soup=BeautifulSoup(html,'lxml')
result=soup.find_all('img')
for link in result:
    link=link.get('data-lazy') or link.get('src')
    t = Thread(target=download_pic, args=(link,))
    t.start()

