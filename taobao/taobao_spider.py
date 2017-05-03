#!/usr/bin/env python
# coding=utf-8

import sys,os
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], '../submodules'))

import requests
import re

from Common.useful import paser_urls

class TaobaoSpider(object):

    def __init__(self,index_url):
        self.index = index_url
        self.host = "taobao.com"

    def get_urls(self):
        content = self.get_html()
        content = content.replace("{host}",self.host)
        urlParttern = r'\/\/[\w\-\/]+[\.[\w\-\/]+]*'
        pattern = re.compile(urlParttern)
        urls1 = re.findall(pattern,content,0)
        urls3 = []
        for u in urls1:
            url = "https:" + u
            urls3.append(url)

        urls2 = paser_urls(content)
        urls = urls3 + urls2
        urls4 = []
        for u in urls:
            if "tmall.com" in u or "taobao.com" in u:
                urls4.append(u)
        return urls4

    def get_html(self):
        r = requests.get(self.index)
        return r.content
