#!/usr/bin/env python
# coding=utf-8
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"}
url = "http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=600002"
r = requests.get(url,headers = headers)
html = r.content
print html
