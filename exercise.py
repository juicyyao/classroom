# -*- coding: utf-8 -*-
import urllib.request
url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib.request.urlopen(url1).read().decode('utf8')
provinces = content1.split(',')
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces[1:]:
    p_code = p.split('|')[0]#获得省的编号如[01]
    url2 = url % p_code#http://m.weather.com.cn/data3/city02.xml
    #content2 = urllib.request.urlopen(url2).read().decode('utf8')
    a=urllib.request.urlopen(url2)
    b=a.read()
    content2=b.decode('utf8')#获得每个省的各个市的名字如<class 'str'> 0501|哈尔滨
    cities = content2.split(',')#字符串转换成列表如['0101|北京']
    for c in cities:
        c_code = c.split('|')#城市分割放进列表
        url3 = url % c_code[0]#http://m.weather.com.cn/data3/city0101.xml
        content3 = urllib.request.urlopen(url3).read().decode('utf8')
        districts = content3.split(',')

        for d in districts:
            d_pair = d.split('|')#['010101', '北京']
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            try:
                content4 = urllib.request.urlopen(url4).read().decode('utf8')
                #print (content4)
                code = content4.split('|')[1]
                line = "    '%s': '%s',\n" % (name, code)
                result += line
                print(name + ':' + code)
            except:
                pass




result += '}'
f = open('cities.py', 'w')
f.write(result)
f.close()