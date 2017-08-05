# coding=utf-8
n=int(raw_input('输出几项：'))
list=[]
a = 1
b = 1
list.append(a)
list.append(b)
for i in range(n-2):
    list.append(list[i]+list[i+1])
for j in list:
    print j

n=input()
x=3
a1=1
a2=1
while x <=n:
    a3=a1+a2
    print a3
    a1=a2
    a2=a3
    x+=1