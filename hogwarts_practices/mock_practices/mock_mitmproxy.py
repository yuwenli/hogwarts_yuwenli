#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/23 12:33
# @Author  : yuwenli
import json

from mitmproxy import http
from mitmproxy import ctx

"""
采取修改响应数据，第一个股票保持不变，第二个股票名字增长1倍，第三个股票名称为空
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
            # 修改原始数据
            data = json.loads(flow.response.text)
            items = data["data"]["items"]
            # 第二个股票名字增长1倍
            items[1]["quote"]["name"] += items[1]["quote"]["name"]
            # 第三个股票名字置空
            items[2]["quote"]["name"] = ""
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]