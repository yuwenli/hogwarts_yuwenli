#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 16:27
# @Author  : yuwenli
from appium.webdriver.common.mobileby import MobileBy

from appium_20210303.page.base_page import BasePage

"""
page:打卡页面,分为上下班打卡,外出打卡
function1:外出打卡,外出打卡验证
"""


class SignPage(BasePage):
    # 外出打卡
    def sign_outplace(self):
        self.steps(self.data_path, "sign")

    def get_sign_outplace(self):
        # 外出打卡：获取打卡后的提示
        element = self.steps(self.data_path, "sign_outplace_data")
        return element.get_attribute('text')