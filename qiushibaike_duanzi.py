import requests
from lxml import etree
n=int(input('how many page do you want to get :'))

url='https://www.qiushibaike.com/'
k=2
data_all=''
for page in range(n):
    req=requests.get(url)
    html=req.text
    tree=etree.HTML(html)
    result=tree.xpath('//div[@class="article block untagged mb15 typs_hot"]')
    for i in result:
        author=i.xpath('.//h2/text()')
        author =author[0].strip('\n')
        if author !='匿名用户':
            age=i.xpath('.//div[@class="author clearfix"]/div/text()')[0]
            gender=i.xpath('.//div[@class="author clearfix"]/div/@class')[0]
            if gender== 'articleGender manIcon':
                author_gender='男'
            else:
                author_gender = '女'
        else:
            age='无'
            auther_gender='无'


        vote=i.xpath('.//div[@class="stats"]/span/i/text()')

        content=i.xpath('.//div[@class="content"]/span/text()')
        comment=i.xpath('.//div[@class="stats"]/span/a/i/text()')

        author='作者：'+author
        data_all +=author+'\n'
        data_all += '性别：'+author_gender + '\n'
        data_all+='年龄：'+age+'\n'
        content = '段子：' + content[0].strip('\n')
        data_all += content + '\n'
        vote='好笑数：'+vote[0]
        data_all+=vote+'\n'
        comment='评论数：'+comment[0]
        data_all += comment + '\n'+'========================='+'\n'
    url='https://www.qiushibaike.com/8hr/page/%d/' % k
    data_all+='******'+'PAGE:'+str(k-1)+'******'+'\n'
    k=k+1
with open('jokess.txt','w',encoding='utf-8') as f:
    f.write(data_all)