#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 23:17
# @Author  : 日积跬步
# @File    : osModuleOpe.py

"""os 常用模块"""

import os

# 返回当前的工作目录
print(os.getcwd())

print('-----')
# 返回指定目录下的文件和目录信息
print(os.listdir(os.getcwd()))

print('-----')
# 创建目录
# os.mkdir('osMkDir')
os.makedirs('a/b/c')

# 删除目录
# os.rmdir(os.getcwd() + '\\osMkDir')
# os.removedirs('a/b/c')
print(os.getcwd() + '\\abc')

# 将path设置为当前工作目录
# os.chdir('')

