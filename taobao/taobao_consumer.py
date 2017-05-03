#!/usr/bin/env python
# coding=utf-8

import sys,os
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], '../submodules'))

import json
from Common.queues.rb_consumer import RQConsumer
from Common.queues.rb_product import RQProduct
from taobao_spider import TaobaoSpider

class TaobaoConsumer(RQConsumer):

    def __init__(self,rq_queue,rq_host="127.0.0.1",rq_port=5672,kwags={}):
        self.p = RQProduct(rq_queue,rq_host,rq_port)
        RQConsumer.__init__(self,rq_queue,rq_host,rq_port,kwags)

    def data_process(self,data):
#        return
        j_data = json.loads(data)
        url = j_data["url"]
        taobao_spider = TaobaoSpider(url)
        rep_urls = taobao_spider.get_urls()
        for u in rep_urls:
            print u

if __name__ == "__main__":
    from Common.queues.rb_consumer import TestConsumer
    TestConsumer(TaobaoConsumer,"url_queues5","127.0.0.1","5672")


