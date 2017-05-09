#!/usr/bin/env python
# coding=utf-8


import requests
import uuid
import json

url = "http://weibo.com/starbucks?refer_flag=1001030101_&is_hot=1"

r = requests.get(url)
#print r.content
html = r.content.decode("gbk")
print html

#url = "http://weibo.com/js/visitor/mini_original.js?v=20161116"

#r = requests.get(url)
#print r.content
