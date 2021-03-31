#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/30 17:32
# @Author  : yuwenli
import pytest
import requests
import yaml

"""
获取token
"""


class Base:
    def __init__(self):
        self.s = requests.session()
        # 调用获取token方法
        self.token = self.get_token()
        # 将token存在session中
        self.s.params = {"access_token": self.token}

    def send_contact(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)

    # 封装send发送请求方法和yaml参数化接口
    def send(self, path, interface_class, interface_para):
        # s.get()或者s.post底层用的还是request
        # self.s.request('GET', url, **kwargs)
        with open(path, 'r', encoding='utf-8') as f:
            data_test = yaml.safe_load(f)
            info: list = data_test[interface_class]
            for i in info:
                # print(i)
                for key, value in i.items():
                    api_url = i.get('url')
                    data = i.get('data')
                    method = i.get('method')
                    expect = i.get('expect')
                    if value == interface_para:
                        if method == 'POST':
                            return self.s.request('POST', url=api_url, json=data), expect
                            break
                        elif method == 'GET':
                            return self.s.request('GET', url=api_url, params=data), expect
                            break

    # 获取token
    def get_token(self):
        # 获取token
        corpsecret = "GtPkHRci3tuhiQTUF_NXyCQ_zcWbFzY-vVX1yfJ325E"
        corpid = "ww84ea8fdfa733aac4"
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        data = {"corpid":corpid, "corpsecret":corpsecret}
        r = requests.get(url=url, params=data)
        # print(r.text)
        # print(r.json())
        token = r.json()['access_token']
        return token