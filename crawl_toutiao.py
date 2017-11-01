import requests
import csv
url_1='https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time='

headers={
'Cookie':'uuid="w:3ab8841984904754bac344e6107d0a5a"; UM_distinctid=15f762a3afb3a-078fc3475a47ec-396b4c0b-100200-15f762a3afdc8; __tasessionId=895rr8s051509515998496; CNZZDATA1259612802=2114542959-1509511754-null%7C1509511754; tt_webid=6483321851858765326',
'Host':'www.toutiao.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
url=url_1+'1509518597'
all_content=[]
for i in range (5):
    print (url)
    req=requests.get(url,headers=headers)
    content=req.json()

    for item in content['data']:
        try:
            title=item['title']
            abstract=item['abstract']
            comments_count=item['comments_count']
            print ('title:',title)
            print ('abstract:',abstract)
            print ('comments_count：',comments_count)
        except Exception as e:
            print (e)
            continue
        all_content.append([title, abstract, comments_count])

    print('=====================================')
    next=content['next']
    url=url_1+str(next['max_behot_time'])

with open ('today_headline.csv','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['title','abstract','comments_count'])
    for data in all_content:
        writer.writerow(data)