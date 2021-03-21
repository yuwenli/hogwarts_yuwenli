#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/19 18:35
# @Author  : yuwenli
from selenium.webdriver.common.by import By

from appium_20210303.page.base_page import BasePage

"""
page:个人信息编辑页面
function:联系人编辑页面,可编辑和删除联系人
待优化:编辑,替换yaml中内容
"""


class EditContactPage(BasePage):

    # 编辑成员,修改成员姓名和性别
    def edit_contact(self, update_data):
        self._params = update_data
        # self.find(By.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(new_name)
        # self.find(By.ID,"dux").click()
        # self.find(By.XPATH, "//*[@text='男']").click()
        self.steps(self.data_path, "edit_contact")
        # 提交信息
        self.steps(self.data_path, "save_contact")

    # 个人信息:编辑成员页面,选择删除成员
    def delete_contact(self):
        self.steps(self.data_path, 'delete_contact')