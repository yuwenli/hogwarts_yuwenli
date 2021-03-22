#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 16:07
# @Author  : yuwenli

from appium_20210303.page.base_page import BasePage
from appium_20210303.page.contact.listContact_page import MemberPage
from appium_20210303.page.workbanch.workbanch_page import WorkBanchPage

"""
page:进入主页
主页包含工作台,通讯录,我,消息
"""


class MainPage(BasePage):
    def goto_workbanch(self):
        # 进入工作台页面
        self.steps(self.data_path, "goto_workbanch")
        return WorkBanchPage(self._driver)

    def goto_contact(self):
        # 进入通讯录页面
        self.steps(self.data_path, "goto_contact")
        return MemberPage(self._driver)