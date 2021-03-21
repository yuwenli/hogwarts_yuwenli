#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 16:17
# @Author  : yuwenli


from appium_20210303.page.base_page import BasePage
from appium_20210303.page.workbanch.sign_page import SignPage

"""
page:工作台页面
function1:进入打卡页面
"""


class WorkBanchPage(BasePage):
    def goto_sign(self):
        # 点击打卡,进入打卡页面
        self.find_by_scroll("打卡")
        return SignPage(self._driver)
