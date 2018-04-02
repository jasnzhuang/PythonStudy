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


class Person:
    name = "mmy"
    age = 19
    sex = "female"

    def call_name(self):
        print("My name is {}".format(self.name))


bread = Person()
# bread.name = "cat"
# bread.age = 0.1
# bread.sex = "male"

print(Person.name + " have a " + bread.name)
my_object = Person()
my_object.call_name()
bread.call_name()
