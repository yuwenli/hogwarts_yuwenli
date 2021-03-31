#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/30 10:22
# @Author  : yuwenli
import requests


def get_token(self):
    # 获取token
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww84ea8fdfa733aac4&corpsecret=nTeFlUJaQ4tqIHJGrEaknzi5jbRWGxj2FFFMUEFC7iU")
    # print(r.text)
    # print(r.json())
    self.token = r.json()['access_token']
    return self.token