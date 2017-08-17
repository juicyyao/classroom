# -*- coding:utf-8 -*- 
import requests
import json
word=raw_input('你想查看哪个城市的天气：\n')
url='http://wthrcdn.etouch.cn/weather_mini?city=%s' % word
req=requests.get(url)
req.encoding ='utf-8'
req=req.json()
result = req['data']
result1=result['forecast']
result2=result1[0]
str_temp = ('%s\n%s ~ %s') % (
result2['type'],
result2['low'],
result2['high'])
print str_temp
