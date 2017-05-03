#!/usr/bin/env python
# coding=utf-8

import sys,os
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], '../submodules'))

from Common.queues.rb_product import RQProduct
                 
p = RQProduct("url_queues5")
def send(n):        
    for i in range(n):
        msg = {"url":"https://taobao.com"}
        p.product(msg)
        print msg
                 
send(1)
