#!/usr/bin/env python
# coding=utf-8
"""
    http://www.sse.com.cn/
    该文件包含解析上海证券交易所的网页页面的类
"""

from bs4 import BeautifulSoup

class SSEParser():
    def __init__(self):
        pass

    def stock_page_parser(self,html):
        bs = BeautifulSoup(html,"html.parser")
