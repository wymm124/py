#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 11:25
# @Author  : 日积跬步
# @File    : db7.py
import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    print("连接数据库成功")
    cur = db.cursor()
    sql = 'drop table if exists student'
    cur.execute(sql)
    print("删除数据表成功")
except pymysql.Error as e:
    print("删除数据表失败" + str(e))
