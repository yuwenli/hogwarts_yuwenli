#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/24 20:15
# @Author  : yuwenli


from Animcal import Animal


class Cat(Animal):
    def __init__(self):
        self.hair = "shot hair"

    def catchMice(self):
        # print(self.name)
        print("it can catch mice")

    def bark(self):
        print("miao miao")
