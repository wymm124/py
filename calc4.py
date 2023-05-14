#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 23:43
# @Author  : 日积跬步
# @File    : calc4.py

"""以主程序方式运行"""


def add(a, b):
    return a + b


# 以主程序方式运行, 只有在运行 calc4 时, 才会进行调用 print 方法
if __name__ == '__main__':
    print(add(10, 20))

