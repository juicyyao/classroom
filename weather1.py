# -*- coding: utf-8 -*-
from city import city
import urllib2
from StringIO import StringIO
import gzip
import json
cityname=raw_input('你想查哪个城市的天气？\n')
citycode=city.get(cityname)
if citycode:
    try:
        url= ('http://wthrcdn.etouch.cn/weather_mini?citykey=%s' % citycode)
        content=urllib2.urlopen(url).read()
        buf = StringIO(content)
        f = gzip.GzipFile(fileobj=buf)
        content = f.read()
        data1 = json.loads(content)

        result = data1['data']
        result1=result['forecast']
        result2=result1[0]
        str_temp = ('%s\n%s ~ %s') % (
            result2['type'],
            result2['low'],
            result2['high'])
        print str_temp
    except:
        print '查询失败'
else:
    print '没有找到该城市'
