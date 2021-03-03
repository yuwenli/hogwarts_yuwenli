#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 11:18
# @Author  : yuwenli
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumPOPractices.page.base_page import BasePage

"""
添加成员page
"""


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member(self, username, account, phonenum):
        # username = "测试1"
        # account = "test01"
        # phonenum = "18898426547"
        # 添加姓名
        self.find(By.ID, "username").send_keys(username)
        # 添加账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入手机号
        self.find(By.CSS_SELECTOR, '.ww_telInput_mainNumber').send_keys(phonenum)
        # 点击保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        """
        获取所有联系人姓名
        :return:
        """
        locator_element = (By.CSS_SELECTOR, ".ww_checkbox")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_element))
        # pages = self.finds(By.CSS_SELECTOR,'.ww_pageNav_info_text')
        # print(f"pages:{pages}")
        element_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for ele in element_list:
            names.append(ele.get_attribute("title"))
        return names