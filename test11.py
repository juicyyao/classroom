import os

path='D:\Test'

for root,dirs,files in os.walk(path):
    print ('root=',root,'dirs=',dirs,'files=',files)
