#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 10:54
# @Author  : 日积跬步
# @File    : db2.py

import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    print("连接数据库成功")
    cur = db.cursor()
    cur.execute('drop table if exists student')
    sql = 'create table student (name varchar(20), email varchar(20), age int)'
    cur.execute(sql)
    print("表创建成功")
except pymysql.Error as e:
    print("创建数据表失败" + str(e))
