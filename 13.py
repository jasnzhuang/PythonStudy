#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Jason'
__mtime__ = '2017/10/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


class Student:
    def __init__(self):
        self.name = "初始name"
        self.grade = "幼稚园"
        self.district = "孤家子"


class Student2:
    def __init__(self, name="初始name2", grade="幼稚园2", district="孤家子2"):
        self.name = name
        self.grade = grade
        self.district = district


test = Student()
print(test.name)
test2 = Student2()
print(test2.name)
test3 = Student2(name="新朋友", grade="上小学的", district="铁西那嘎达")
print(test3.name)
