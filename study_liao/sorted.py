#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:18
# @Author  : 日积跬步
# @File    : sorted.py

# sorted 排序，可以传入key函数，实现自定义排序；可以传入reverse参数，决定是否反转

# 内置sorted函数
def func_sorted():
    lst = [1, 99, 56, 78, 20]
    print(sorted(lst))


# 传入key函数：abs绝对值函数
def func_key():
    lst = [-10, 5, 34, 89, 99, 108]
    print(sorted(lst, key=abs))


def func_key_str():
    lst = ['apple', 'banana', 'boB', 'Alice', 'Zoo']
    print(sorted(lst, key=str.lower))


def func_key_reverse():
    lst = [-10, 5, 34, 89, 99, 108]
    print(sorted(lst, key=abs, reverse=True))


if __name__ == '__main__':
    # func_sorted()
    # func_key()
    # func_key_str()
    func_key_reverse()
