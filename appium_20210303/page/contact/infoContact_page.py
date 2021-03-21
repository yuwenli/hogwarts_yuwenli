#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/19 18:04
# @Author  : yuwenli

from appium_20210303.page.base_page import BasePage
from appium_20210303.page.contact.editContact_page import EditContactPage

"""
page:个人信息页面
function:
"""


class ContactInformationPage(BasePage):
    # 个人信息页面:点击编辑,进入编辑页面
    def contact_detail_setting(self):
        self.steps(self.data_path, 'contact_detail_setting')
        return EditContactPage(self._driver)