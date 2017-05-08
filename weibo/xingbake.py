#!/usr/bin/env python
# coding=utf-8

import requests
import httplib
import uuid
httplib.HTTPConnection.debuglevel = 1

def get_SUB():
    uid = uuid.uuid1()
    uid = str(uid)
    a = uid[:4]
    uid2 = uuid.uuid1()
    uid2 = str(uid2)
    b = uid2[:33]
    return "SUB=_2AkMuTM" + a + "NxqwJRmP8SxGnlboR-yQ3EieKYEDg_JRMxHRl-yT83q" + b + "..;"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, compress",
    "Accept-Language": "en-us;q=0.5,en;q=0.3",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Upgrade-Insecure-Requests":"1",
}
SUB = get_SUB()
headers["Cookie"]=SUB
url = "http://weibo.com/starbucks?refer_flag=1001030101_&is_hot=1"

r = requests.get(url,headers = headers,allow_redirects = False)

html = r.content
print(html)
