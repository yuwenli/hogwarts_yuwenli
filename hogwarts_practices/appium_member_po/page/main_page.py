#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 16:07
# @Author  : yuwenli
from appium.webdriver.common.mobileby import MobileBy

from appium_20210303.page.base_page import BasePage
from appium_20210303.page.member_page import MemberPage
from appium_20210303.page.workbanch_page import WorkBanchPage


class MainPage(BasePage):
    def goto_workbanch(self):
        # 进入工作台页面
        self.find(MobileBy.XPATH, "//*[@text='工作台']").click()
        return WorkBanchPage(self._driver)

    def goto_contact(self):
        # 进入通讯录页面
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return MemberPage(self._driver)