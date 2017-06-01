# -*- coding:utf-8 -*-
import requests
import re
import random
import MySQLdb
from bs4 import BeautifulSoup
import time

class house():
    def get_house(self):
        user_agent = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
            ]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': user_agent[random.randint(0, 5)]
        }
        list = []
        for i in range(1, 16):
            if i==1:
                url = 'https://bj.lianjia.com/xiaoqu/daxing/'
            else:
                url = 'https://bj.lianjia.com/xiaoqu/daxing/pg' + str(i) + '/'
            r = requests.get(url, headers=headers)
            r.encoding = 'utf8'
            html = r.text
            soup = BeautifulSoup(html)

            for tag in soup.find('ul', class_='listContent').find_all('li', class_="clear xiaoquListItem"):
                ss = []
                for aa in tag.find_all('a'):
                   # print aa.string
                    ss.append(aa.string)

                for bb in tag.find_all('span'):
                  #  print bb.string
                    ss.append(bb.string)
                #print len(ss)
                ss[0]=time.strftime("%Y-%m-%d",time.localtime(time.time()))
                list.append(ss)

        for item in list:
            for element in item:
                print element,
            print "\n"


test = house()
test.get_house()