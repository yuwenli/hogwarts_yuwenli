#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 11:18
# @Author  : yuwenli

"""
主页
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from seleniumPOPractices.page.add_member_page import AddMemberPage
from seleniumPOPractices.page.base_page import BasePage


class MainPage(BasePage):
    # base_url不为空时，直接通过该url访问
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加member
        :return:
        """
        # 点击添加成员
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # return到add_member_page
        return AddMemberPage(self.driver)
