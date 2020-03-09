#!/usr/bin/python3

import requests
import json
import lxml
from time import sleep
import urllib.parse
from bs4 import BeautifulSoup
import sys
import os

def objectid(strings):
    soup = BeautifulSoup(strings, 'lxml')
    anss=[]
    for i in list(soup.select('script')):
        #    print(i)
        ss = str(i)
        if ss.find('function()') != -1:
            ii = ss.split('try{')[1]
            ii = ii.lstrip()
            ii = ii.split('}catch')
            ii = ii[0].split('=', 1)[1]
            ii = ii.split(';')[0]
            ii = str(ii)
            try:
                text = json.loads(ii)
                for dic in text['attachments']:
                    if dic['property']['module']=='insertdoc'or dic['property']['module']=='insertvideo':
                        anss.append(dic['property']['objectid'])
            except:
                anss=[]
    return anss

def get_cookie(strr):
    cookie_dict = {}
    s = strr.split(';')
    for i in s:
        key, value = i.lstrip().split('=', 1)
        cookie_dict[key] = value
    return cookie_dict

if __name__ == '__main__':
    print('请输入要抓取的课程链接:')
    url=input('> ')
    query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
    courseid=str(query['courseId'])
    clazzid=str(query['clazzid'])
    knows=[]
    ans=[]
    url='https://mooc1-1.chaoxing.com/mycourse/studentstudycourselist?courseId='+courseid+'&clazzid='+clazzid
    print('请输入cookies:')
    strr = input('> ')
    cookie_dict=get_cookie(strr)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, cookies=cookie_dict)
    soup=BeautifulSoup(response.text.encode('utf8'),'lxml')

    for i in soup.select('a'):
        ss=str(i['href'])
        know=ss.split('(')[1].split(')')[0].split(',')[-1]
        know=know[1:-1]
        knows.append(know)

    for i in knows:
        url='https://mooc1-1.chaoxing.com/knowledge/cards?clazzid='+clazzid+'&courseid='+courseid+'&knowledgeid='+str(i)
        sleep(0.5)
        response = requests.request("GET", url, headers=headers, cookies=cookie_dict)
        tmp=objectid(response.text.encode('utf8'))
        ans+=tmp
        
    f = open("output.txt", "w")
    for i in ans:
        f.write('http://cs.ananas.chaoxing.com/download/'+str(i)+'\n')
    f.close()



