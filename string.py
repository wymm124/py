#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 23:27
# @Author  : 日积跬步
# @File    : string.py

# 字符串的驻留机制（pycharm 对 str 进行了优化）
print('驻留机制')
s1 = 'abc%'
s2 = 'abc%'
print(s1 is s2)

# 常用操作
print('常用操作')
s3 = 'hello world hello'
print(s3.index('llo'))  # 2
print(s3.rindex('llo'))  # 14
# print(s3.index('ok'))  # error
# print(s3.rindex('ok'))  # error
print(s3.find('ok'))  # -1
print(s3.rfind('ok'))  # -1


# 大小写转换
print('大小写转换')
s4 = 'this is just A test'
print(s4.upper())
print(s4.lower())
print(s4.swapcase())
print(s4.capitalize())
print(s4.title())

# 对齐方式
print('对齐方式')
s5 = 'hello,world'
# 居中对齐
print(s5.center(20, '*'))
# 左、右对齐
print(s5.ljust(30, '$'))
print(s5.rjust(30, '$'))
# 右对齐，用0填充
print(s5.zfill(30))
print('-1234'.zfill(10))

# 分割
print('分割方法')
s6 = 'hello world python'
# 默认空格分割符
print(s6.split())
# maxsplit：最大分割次数，sep：自定义分隔符
print(s6.split(sep=' ', maxsplit=1))
print('hello|world|python'.split(sep='|', maxsplit=1))
# 从右侧分割
print(s6.rsplit(' ', maxsplit=1))


# 判断
s7 = '张三'
# 是不是合法的标识符
print(s7.isidentifier())
# 是否全部由空白字符组成（回车，换行，水平制表符）
print(s7.isspace())
# 是否全部为字母组成
print(s7.isalpha())
# 是否全部为十进制的数字组成
print(s7.isdecimal())
# 是否全部由数字组成
print(s7.isnumeric())
# 是否全部由字母和数字组成
print(s7.isalnum())
print('张三123'.encode('utf-8'))
print('张三123'.encode('utf-8').isalnum())


# 替换、合并
s8 = 'hello world'
print(s8.replace(' ', '-'))
# 限制替换的次数
print('hello, hello, hello python'.replace('hello', 'haha', 2))
# 将列表或元组中的字符串合并成一个字符串
lst = ['a', 'b', 'c', 'd']
print('-'.join(lst))
t = ('1', '2', '3', '4')
print('*'.join(t))


# 比较操作
s9 = 'apple'
s10 = 'banana'
print(s9 > s10)
print(ord('a'))
print(ord('b'))
print(ord('王'))
print(chr(29579))


# == 与 is 的区别
a = b = 'python'
c = 'python'
print(a == b)
print(a == c)
print(a is c)
print(id(a))
print(id(c))


# 切片

# 格式化字符串
print('格式化字符串')
name = '张三'
age = 30
print('测试%占位符')
print('我叫%s, 今年%d岁' % (name, age))
print('测试{}占位符')
print('我叫{0}, 今年{1}岁, 我真的叫{0}'.format(name, age))
print('f-string方法')
print(f'我叫{name}, 今年{age}岁。。。')



