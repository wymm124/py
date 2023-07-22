#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 10:26
# @Author  : 日积跬步
# @File    : db1.py
import pymysql
import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    print("数据库连接成功")
except pymysql.Error as e:
    print("连接数据库发生异常" + str(e))
