#!/usr/bin/env python
# -*- coding:utf-8 -*-


saved_money = 1000


def send_money():
    # 发工资
    global saved_money
    saved_money = 2000
    return saved_money


def select_money():
    # 查询工资
    money = saved_money
    return money
