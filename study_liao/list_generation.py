#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 21:55
# @Author  : 日积跬步
# @File    : list_generation.py

# 列表生成式：用来创建list的生成式；如果if在for前边，必须加else（if...else是表达式）；如果if在for后边，不用加else（if是for的过滤，不用带else）
def prac_gene1():
    lst = list(range(6))
    print(lst)


def prac_gene2():
    lst = [i * i for i in range(5)]
    print(lst)


def prac_gene3():
    lst = [i * i for i in range(8) if i % 2 == 0]
    print(lst)


def prac_gene4():
    lst = [x + y for x in 'abc' for y in 'lmn']
    print(lst)


def prac_gene5():
    d = {'a': 1, 'b': 2, 'c': 3}
    for k, v in d.items():
        print('{} = {}'.format(k, v))


def prac_gene6():
    lst = [i if i % 2 == 0 else -i for i in range(9)]
    print(lst)


if __name__ == '__main__':
    # prac_gene1()
    # prac_gene2()
    # prac_gene3()
    # prac_gene4()
    # prac_gene5()
    prac_gene6()

    # for i in range(4):
    #     print(i)
