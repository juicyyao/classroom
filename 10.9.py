# coding =utf-8
import re
with open('words.txt','r') as f :
    word=f.read()
result=re.findall(r'\b[A-z]+\b',word)
num=len(result)
print ('There are %d words in words.txt' % num)