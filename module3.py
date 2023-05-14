#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 23:33
# @Author  : 日积跬步
# @File    : module3.py

"""导入自定义模块中的指定内容"""
from calc import div

print('调用自定义模块中的指定函数')
res = div(40, 8)
print(res)

