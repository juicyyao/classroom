#coding=utf-8
import operator
scores=[]
result=[]
#打开文件
with open('report.txt','r') as f:
    lines=f.readlines()#输出以每个人名字和成绩为元素的列表
    len=len(lines)#计算元素的个数

#计算总成绩和平均分
for line in lines:
    scores=line.split()#将每个元素的字符串类型转化成列表
    sum=0
    avg=0
    for i in scores[1:]:
        sum+=int(i)#字符串转化成数字
        avg=round(float(sum)/9,1)#平均数保留一位小数
    scores.append(str(sum))
    scores.append(str(avg))#将总分和平均数加到每位同学的列表中
    result.append(scores)#将每位同学的列表放进大列表中，形成嵌套列表，给自己挖了一个大坑啊
#按平均分从高到低排列
result.sort( key=operator.itemgetter(11),reverse=True)#网上搜的模块，可以对嵌套列表中平均数元素进行排序
#汇总各科平均分和总平均分
avg_=[]
for i in range(1,12):
    sum_1=0
    for j in result:
        sum_1+=float(j[i])#求各科的总分
    if i <11:
        avg_.append(str(int(sum_1/len)))#求各科的总平均分，并转化成字符，放入平均数列表
    else:
        avg_.append(str(round(float(sum_1 / len),1)))
avg_.insert(0,'平均')#在平均数列表中首项中添加‘平均’这个元素
result.insert(0,avg_)#把平均数这个列表加入到总的result列表首项
#将小于60分替换成‘不及格’
for a in range(len+1):
    for b in range(1,12):
        if float(result[a][b])<60:#列表中元素转化成数字比较是否小于60
            result[a][b]='不及格'

#插入名次
rank=0
while rank <=int(len):
    for letter in result:
        letter.insert(0,str(rank))#在每个元素的首项插入名次
        rank=rank+1
#加入标题
title=['名次','姓名','语文', '数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
result.insert(0,title)#标题加入到result列表中首项
#把result列表变成字符串，防止用列表写入文件时只能显示最后一行
final_result=''
for d in result:
    liness='\t'.join(d)+'\n'#把每个小列表转化成字符串
    final_result+=liness#把每个字符串拼接成大字符串
#写入文件
f =open ('final_result.txt','w')
f.write(final_result)
f.close