#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 16:27
# @Author  : yuwenli
from appium.webdriver.common.mobileby import MobileBy

from appium_20210303.page.base_page import BasePage


class DakaPage(BasePage):
    # 外出打卡
    def daka_out(self):
        self.find(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.find(MobileBy.XPATH,'//*[contains(@text,"次外出")]').click()

    def get_daka_out_data(self):
        # 外出打卡：获取打卡后的提示
        return self.find(MobileBy.ID, 'mn').get_attribute('text')