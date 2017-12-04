from selenium import webdriver
import time
import requests
def get_img(img_url,filename):
    content=requests.get(img_url).content
    with open (filename,'wb') as f:
        f.write(content)

from bs4 import BeautifulSoup
url='http://zu.sh.fang.com/'
driver=webdriver.PhantomJS(service_args=['--load-images=no'])
driver.get(url)
driver.find_element_by_id('input_key').send_keys('闵行')
driver.find_element_by_id('rentid_39').click()
time.sleep(1)
for i in range(5):

    soup=BeautifulSoup(driver.page_source,'lxml')
    items=soup.find_all(class_="list hiddenMap rel")
    for item in items:
        price=item.find(class_='price').get_text()
        img_url=item.find('img').get('data-src')
        address=item.find(class_='gray6 mt20').get_text()
        filename='fang/'+address+price+'一月'
        get_img(img_url,filename)
        print (img_url,'succeed')
    driver.find_element_by_link_text('下一页').click()




