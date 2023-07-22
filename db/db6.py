#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 11:23
# @Author  : 日积跬步
# @File    : db6.py
import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    print("连接数据库成功")
    cur = db.cursor()
    sql = 'delete from student where name = %s'
    value = "jack"
    cur.execute(sql, value)
    # 记得commit，否则数据 delete 不掉
    db.commit()
    print("删除数据成功")
except pymysql.Error as e:
    print("删除数据失败" + str(e))
    db.rollback()

db.close()

