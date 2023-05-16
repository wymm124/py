#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 0:28
# @Author  : 日积跬步
# @File    : scheduleTest.py
import time
import schedule


def job():
    print('haha')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

