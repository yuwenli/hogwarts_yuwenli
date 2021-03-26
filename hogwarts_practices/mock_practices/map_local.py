#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/23 17:03
# @Author  : yuwenli



import json

from mitmproxy import http
from mitmproxy import ctx

"""
采用递归方法
"""


class Counter:
    def __init__(self):
        self.num = 0

    # 每一次请求都会调用此函数
    def request(self, flow:http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    # 对响应进行修改，则在response中进行修改
    def response(self,flow):
        # 判断是否是想要的请求信息，通过url进行判断
        url_test = "https://stock.xueqiu.com/v5/stock/batch/quote.json?"
        if url_test in flow.request.pretty_url:
            with open("./mock.json", encoding="utf-8") as f:
                # 获取json文件内容
                data = json.load(f)
            # json.dumps()转换为字符串
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]