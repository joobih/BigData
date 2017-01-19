#!/usr/bin/env python
# coding=utf-8

import requests
from wangyi_parser import WangYiParser

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"}

#url = "http://money.163.com/17/0111/15/CAGPOLMC0025814T.html"
#url = "http://money.163.com/17/0111/05/CAFPK523002580S6.html"
url = "http://money.163.com/17/0111/20/CAHCADBA002580S6.html"
r = requests.get(url,headers = headers)

parser = WangYiParser()
result = parser.news_page_parser(r.content.decode("gbk"))
print result
print result["time"],result["from"],result["title"],result["editor"],result["make_time"],result["text"]
