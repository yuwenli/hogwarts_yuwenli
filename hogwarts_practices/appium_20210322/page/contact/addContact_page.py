#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/21 20:24
# @Author  : yuwenli
from appium_20210303.page.base_page import BasePage


class AddContactPage(BasePage):
    # 提交联系人信息
    def add_member_information_submit(self, contact_params):
        self._params = contact_params
        print(self._params)
        # 联系人信息填写
        self.steps(self.data_path, "add_member")
        # 提交信息
        self.steps(self.data_path, "save_contact")