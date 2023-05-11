#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 23:59
# @Author  : 日积跬步
# @File    : class4.py.py

"""如果不希望外部访问对象的某个属性 可以在属性前增加__"""


class Car:
    def __init__(self, brand, money):
        self.brand = brand
        # 不希望外部对象获取到
        self.__money = money

    @classmethod
    def drive(cls):
        print('开车中。。类方法')


car = Car('byd', 20)
print(car.brand)
# 获取对象中的属性和方法
# print(dir(car))

# 不建议这么用
print(car._Car__money)
