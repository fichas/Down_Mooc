# -*- coding: utf-8 -*-
import re
import sys
import os
import requests

headers = {'Referer':'http://d0.ananas.chaoxing.com/','User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}  

url=sys.argv[1]
#print(url)

req = requests.get(url, headers=headers)
strr=req.text


patt=re.compile(r'[a-zA-z]+://cs.[^\s][^\_\$]*')
res=patt.findall(strr)

f=open('output.txt','w')
for i in res :
    f.write(i)
    f.write('\n')
f.close()
patt=re.compile(r'<i[^>]*>(.*?)</i>+<a[^>]*>(.*?)</a>')
res=patt.findall(strr)
f=open('name.bat','w')
for i in res :
    s1=str(i[0])
    s2=str(i[1])
    s1=s1.strip()
    s2=s2.strip()
    stri='ren '+s1+'.mp4 '+s1+'_'+s2+'.mp4'
    f.write(stri)
    f.write('\n')
f.close()

