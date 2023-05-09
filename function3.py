#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 22:14
# @Author  : 日积跬步
# @File    : function3.py

"""函数定义：默认参数值"""


def fun(a, b=10):
    print(a)
    print(b)


fun(1)
print('-----')

fun(1, 2)
print('-----')

"""print函数中的参数 end就是示例，如果不传，则默认是 \n"""
print('hello')
print('world')

print('hello', end="\t")
print('world')
