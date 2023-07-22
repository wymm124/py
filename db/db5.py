#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 11:20
# @Author  : 日积跬步
# @File    : db5.py

import pymysql

host = 'localhost'
db = 'pytest'
user = 'root'
pwd = '124207'

try:
    db = pymysql.connect(host=host, database=db, user=user, password=pwd)
    print("连接数据库成功")
    cur = db.cursor()
    sql = 'update student set email = %s where name = %s'
    value = ("tom@qq.com", "tom")
    cur.execute(sql, value)
    # 记得commit，否则数据 update 不进去
    db.commit()
    print("更新数据成功")
except pymysql.Error as e:
    print("更新数据失败" + str(e))
    db.rollback()

db.close()

