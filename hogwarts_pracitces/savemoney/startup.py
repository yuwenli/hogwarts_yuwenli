#!/usr/bin/env python
# -*- coding:utf-8 -*-


from savemoney import hogwarts_01_money

if __name__ == "__main__":
    # 发工资之前
    print("发工资之前：%s " % hogwarts_01_money.select_money())
    saveMoney = hogwarts_01_money.send_money()
    #  发工资之后
    # print(saveMoney)
    # 查询工资
    # sendMoney = hogwarts_01_money.select_money()
    print("发工资之后：%s " % hogwarts_01_money.select_money())
