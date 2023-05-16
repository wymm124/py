#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/16 23:48
# @Author  : 日积跬步
# @File    : module5.py

"""常用的内置模块（标准库）"""

# py解释器-环境操作 相关
import sys
# 时间 相关
import time
# 操作系统服务功能 相关
import os
# 日期 相关
import calendar
# 读取来自网上的数据 相关
import urllib.request
# 使用 json 序列化-反序列化
import json
# 在字符串中执行正则表达式匹配-替换
import re
# 标准算数运算函数
import math
# 进行精确控制运算精度-有效数位-四舍五入操作的十进制运算
import decimal
# 记录事件-错误-告警-调试信息等日志信息
import logging

print(sys.getsizeof(True))
print(sys.getsizeof(12))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())


# with urllib.request.urlopen('http://python.org/') as response:
#     html = response.read()
#     print(html)
