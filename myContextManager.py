#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 22:58
# @Author  : 日积跬步
# @File    : myContextManager.py

"""
自定义上下文管理器
如果某一个类实现了 __enter__、__exit__ 方法，则该类遵守了上下文管理器协议
该类的实例对象被称为上下文管理器
"""


class MyContextMan(object):

    def __enter__(self):
        print('enter方法 被调用')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法 被调用')

    def show(self):
        print('show方法 被调用')


with MyContextMan() as manager:
    manager.show()
