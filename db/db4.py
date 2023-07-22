#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 11:14
# @Author  : 日积跬步
# @File    : db4.py

import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    cur = db.cursor()
    sql = 'select * from student'
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        name = row[0]
        email = row[1]
        age = row[2]
        print("name: %s, email: %s, age: %s" % (name, email, age))
    print("获取数据成功")
except pymysql.Error as e:
    print("查询数据失败")