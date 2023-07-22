#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 11:01
# @Author  : 日积跬步
# @File    : db3.py

import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    print("连接数据库成功")
    cur = db.cursor()
    sql = 'insert into student(name, email, age) values (%s, %s, %s)'
    value = ("tom", "tom@163.com", 12)
    cur.execute(sql, value)
    # 记得commit，否则数据 insert 不进去
    db.commit()
    print("插入数据成功")
except pymysql.Error as e:
    print("插入数据失败" + str(e))
    db.rollback()

db.close()

