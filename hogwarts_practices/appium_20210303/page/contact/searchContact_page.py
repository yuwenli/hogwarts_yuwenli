#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/21 17:33
# @Author  : yuwenli
from selenium.webdriver.common.by import By

from appium_20210303.page.base_page import BasePage
from appium_20210303.page.contact.infoContact_page import ContactInformationPage


class SearchContactPage(BasePage):
    # 通讯录搜索联系人后,进入个人信息页面
    def search_contact(self, name):
        self._params = name
        self.steps(self.data_path, "search_contact")
        return ContactInformationPage(self._driver)

