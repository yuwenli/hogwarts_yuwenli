#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 17:38
# @Author  : yuwenli
from selenium.webdriver.common.by import By

from appium_20210303.page.base_page import BasePage
from appium_20210303.page.contact.addContact_page import AddContactPage
from appium_20210303.page.contact.infoContact_page import ContactInformationPage
from appium_20210303.page.contact.searchContact_page import SearchContactPage

"""
page:通讯录页面
function1:添加成员(手动添加)-add_memeber_manual
function2:进入个人信息页面
"""


class MemberPage(BasePage):

    # 通讯录列表,点击搜索框后,进入搜索页面
    def enter_search_contact(self):
        self.find(By.ID, 'guu').click()
        return SearchContactPage(self._driver)

    def add_member_method(self):
        # 点击添加成员，进入添加成员页面
        try:
            # 先在页面查找“添加成员”
            self.steps(self.data_path, "add_memeber_main")
        except Exception as e:
            # 未找到则滚动到底部查找
            self.find_by_scroll("添加成员")
        self.steps(self.data_path, "add_memeber_manual")
        return AddContactPage(self._driver)

    def contact_detail(self, value: str):
        # 点击某个联系人,进入个人信息页面
        print(f'value:{value}')
        element = self.find(By.XPATH, f"//*[@text='{value}']")
        # print(element)
        element.click()
        return ContactInformationPage(self._driver)





