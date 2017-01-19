#!/usr/bin/env python
# coding=utf-8

import pysequoiadb
from pysequoiadb import client
from pysequoiadb import const
from pysequoiadb.error import SDBBaseError

class MySequoiadb():
    def __init__(self,cs_name,cl_name):
        try:
            db = client("localhost",11810)
            cs = db.create_collection_space(cs_name)
            self.cl = cs.create_collection(cl_name)
        except (SDBBaseError,Exception) as e:
            msg = "MySequoiadb() init occure a Exception:{}".format(e)
            print msg
            return -10001
    
    def insert(self,data):
        try:
            print data
        except Exception,e:
            msg = "MySequoiadb() insert occure a Exception:{}".format(e)
