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
# os.makedirs('a/b/c')

print('-----')
# 删除目录
# os.rmdir(os.getcwd() + '\\osMkDir')
# os.removedirs('a/b/c')
# print(os.getcwd() + '\\abc')

print('-----')
# 将path设置为当前工作目录
# os.chdir('')

print('-----')
# 获取文件或目录的绝对路径
print(os.path.abspath('osModuleOpe.py'))


print('-----')
# 判断文件或目录是否存在，如果存在返回true，否则返回false
print(os.path.exists('hi.py'))


print('-----')
# 将目录与目录或文件名拼接起来
print(os.path.join('D:\\hello', 'sss.txt'))

print('-----')
# 分离文件名和扩展名
print(os.path.splitext('D:\\Python\\py\\osModuleOpe.py'))

print('-----')
# 从一个目录中提取文件名
print(os.path.basename('D:\\Python\\py\\osModuleOpe.py'))

print('-----')
# 从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('D:\\Python\\py\\osModuleOpe.py'))

print('-----')
# 判断是否为路径
print(os.path.isdir('D:\\Python\\py\\'))



