#!/usr/bin/python3

import requests
import json
import lxml
from time import sleep
import urllib.parse
from bs4 import BeautifulSoup
import sys
import os


class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0
    max_steps = 0
    max_arrow = 50
    infoDone = 'done'

    def __init__(self, max_steps, infoDone = 'Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps)
        num_line = self.max_arrow - num_arrow
        percent = self.i * 100.0 / self.max_steps
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r'
        sys.stdout.write(process_bar)
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0


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

def obj(strings):
    soup = BeautifulSoup(strings, 'lxml')
    anss = []
    for i in list(soup.select('iframe')):
        #    print(i)
        ss=str(i['data'])
        ii=ss
        try:
            text = json.loads(ii)
            anss.append(text['objectid'])
        except:
            anss = []
    return anss

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

    print('获取到 %d 条任务,正在生成下载链接...'%len(knows))

    process_bar = ShowProcess(len(knows), '下载链接已保存到output.txt')
    for i in knows:
        process_bar.show_process()
        url='http://mooc1-1.chaoxing.com/knowledge/cards?clazzid='+clazzid+'&courseid='+courseid+'&knowledgeid='+str(i)
        sleep(0.5)
        response = requests.request("GET", url, headers=headers, cookies=cookie_dict)
        tmp=obj(response.text.encode('utf8'))
        ans+=tmp

    f = open("output.txt", "w")
    for i in ans:
        f.write('http://cs.ananas.chaoxing.com/download/'+str(i)+'\n')
    f.close()



