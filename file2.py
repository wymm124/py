#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 22:53
# @Author  : 日积跬步
# @File    : file2.py

"""
r: 以只读模式打开文件
w: 以只写模式打开文件 如果文件不存在则创建 如果文件存在 则覆盖原有内容
a: 以追加模式打开文件 如果文件不存在则创建
b: 以二进制方式打开文件 不能单独使用 rb wb
+: 以读写方式打开文件 不能单独使用 a+
"""

print('操作文件')
file = open('b.txt', 'a')
file.write('\nhello')
file.close()
