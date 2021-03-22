#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 17:04
# @Author  : yuwenli
from appium_20210303.page.app import App


class TestBase:
    # 所有的测试用例继承TestBase(公共方法的提取）
    # 断言的截图
    app = None
    # path = ""

    def setup_class(self):
        self.app = App()
        # self.path = '../data/data.yaml'
    #
    # def teardown_class(self):
    #     self.app = App()