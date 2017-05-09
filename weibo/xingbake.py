#!/usr/bin/env python
# coding=utf-8

import sys
if sys.version < '3':
    import httplib
    httplib.HTTPConnection.debuglevel = 1
else:
    import http.client
    http.client.HTTPConnection.debuglevel = 1
import requests
import uuid
import json

def get_SUB():
    uid = uuid.uuid4()
    uid = str(uid)
    a = uid[:5]
    uid2 = uuid.uuid4()
    uid2 = str(uid2)
    b = uid2[:33]
#    a = "agEf8"
#    b = "l4BtRC88HwsL0x2TZG0IGt1FJYttFfFjw"
    c = "_2AkMuTagEf8NxqwJRmP8SxGnlboR-yQ3EieKYEVnfJRMxHRl-y"
    d = "T83ql4BtRC88HwsL0x2TZG0IGt1FJYttFfFjw.."
    return "SUB=" + c + d#"NxqwJRmP8SxGnlboR-yQ3EieKYEDg_JRMxHRl-yT83q" + b + "..;"

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
print(headers)
url = "http://weibo.com/starbucks?refer_flag=1001030101_&is_hot=1"

r = requests.get(url,headers = headers,allow_redirects = False)
url = "http://weibo.com/1741514817/ECjM4AH3X?filter=hot&root_comment_id=0&type=comment#_rnd1494297081794"

r = requests.get(url,headers = headers)
#print r.content

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, compress",
    "Accept-Language": "en-us;q=0.5,en;q=0.3",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Upgrade-Insecure-Requests":"1",
    "Cookie":"SUB=_2AkMuTagEf8NxqwJRmP8SxGnlboR-yQ3EieKYEVnfJRMxHRl-yT83ql4BtRC88HwsL0x2TZG0IGt1FJYttFfFjw..;",
}
#SUB = get_SUB()
#headers["Cookie"]=SUB

#url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4091324808745345&from=singleWeiBo&__rnd=1494297081805"
url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4091324808745345&filter=all&from=singleWeiBo&__rnd=1494315362939"
#每个请求结果返回中带着root_comment_max_id 和 type 还有page sum_comment_number 只有from和__rnd参数是自己构造的
url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4091324808745345&root_comment_max_id=4095018229042757&root_comment_max_id_type=&root_comment_ext_param=&page=4&filter=all&sum_comment_number=47&filter_tips_before=1&from=singleWeiBo&__rnd=1494315569076"

r = requests.get(url,headers = headers)
html = r.content
html = json.loads(html)
print(html["data"]["count"])

d = json.dumps(html,ensure_ascii = False)

r = requests.get(url,headers = headers)
html = r.content
html = json.loads(html)
d = json.dumps(html,ensure_ascii = False)
#print(d)



