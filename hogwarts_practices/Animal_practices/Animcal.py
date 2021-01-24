#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/24 19:49
# @Author  : yuwenli


class Animal:
    def __init__(self):
        self.name = "mandy"
        self.color = "white"
        self.age = 3
        self.gender = "male"
        print(f"my cat {self.name},it's {self.color} and {self.age},it's {self.gender}")

    def bark(self):
        print(f"my cat {self.name}  can bark")

    def run(self):
        print("it can run")
