#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 22:27
# @Author  : 日积跬步
# @File    : file4.py

"""
文件对象的常用方法
read([size]) 从文件中读取size个字节或字符返回 省略size则读完
readline() 从文件中读取一行
readlines() 将文本中每一行作为独立的字符串对象 将对象放入列表返回
write(str) 将字符串str内容写入文件
writelines(s_list) 将字符串列表s_list写入文本文件 不添加换行符
seek 把文件指针移动到新的位置
tell 返回文件指针的当前位置
flush 把缓冲区的内容写入文件，但不关闭文件
close 把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源
"""

file = open('a.txt', 'r')
# print(file.read(2))
# file.close()

print('-----')
# print(file.readline())

print('-----')
# print(file.readlines())

file.close()

print('-----')
file2 = open('c.txt', 'w')
# file2.write('hello\nworld')

print('-----')
lst = ['py', 'java', 'ts', 'go']
# file2.writelines(lst)
file2.close()

print('-----')
file3 = open('a.txt', 'r')
# GBK中一个汉字两个字节，如果写成1会报错
file3.seek(2)
print(file3.read())
file3.close()

