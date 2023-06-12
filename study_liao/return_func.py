#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:36
# @Author  : 日积跬步
# @File    : return_func.py

# 返回函数

# 由于返回的函数引用了变量i，但它并非立刻执行，等3个函数都返回后，它们所引用的变量已经变成了3，所以最终结果为9
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# 必须要引用循环变量，则再创建一个方法，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_update():
    def f(m):
        def ff():
            return m * m

        return ff

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


# 闭包：内层函数引用了外层函数的局部变量。如果只是读取外层变量的值，闭包函数正常
def close_package1():
    x = 0
    
    def func():
        return x + 1
    return func


# 如果对外层变量赋值，由于py解释器会把x解释当做函数func的局部变量，则会报错
def close_package2():
    x = 0

    def func():
        # py解释器会把x当做func的局部变量，则表示没有初始化x，会报错，x增加nonlocal声明，py解释器会把x当做外层函数的局部变量，已经被初始化了，可以正常计算
        nonlocal x
        x = x + 1
        return x
    return func


if __name__ == '__main__':
    # f1, f2, f3 = count()
    # print(f1())
    # print(f2())
    # print(f3())

    # f11, f22, f33 = count_update()
    # print(f11())
    # print(f22())z
    # print(f33())

    # f = close_package1()
    # print(f())

    f = close_package2()
    print(f())
