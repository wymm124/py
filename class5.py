#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 0:19
# @Author  : 日积跬步
# @File    : class5.py

"""py中的-多态"""


class Animal(object):
    def eat(self):
        print('动物会吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃饭')


def fun(obj):
    obj.eat()


print('静态语言中的多态, 三个条件: 继承 方法重写 父类引用指向子类对象')
dog = Dog()
fun(dog)
fun(Cat())
fun(Animal())
print('以下是鸭子类型, py中的多态实现, 只关心对象的行为, 不关心对象是什么类型----------')
fun(Person())


