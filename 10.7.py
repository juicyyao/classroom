import re
with open('from.txt','r') as f :
    content=f.read()
result=re.findall(r'[A-z]+',content)
result=sorted(result)
result1=''
for lines in result:
    result1+=lines+'\n'
with open('to.txt','w') as fin:
    fin.writelines(result1)
