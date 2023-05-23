#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 23:17
# @Author  : 日积跬步
# @File    : file3.py

"""操作二进制文件"""

source_file = open('xiao.png', 'rb')
target_file = open('xiao_copy.png', 'wb')
target_file.write(source_file.read())

source_file.close()
target_file.close()

