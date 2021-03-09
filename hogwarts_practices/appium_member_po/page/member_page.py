#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 17:38
# @Author  : yuwenli
from appium.webdriver.common.mobileby import MobileBy

from appium_20210303.page.base_page import BasePage


class MemberPage(BasePage):

    def add_memeber_from_yaml_manual(self):
        # 点击添加成员，进入添加成员页面
        try:
            # 先在页面查找“添加成员”
            element = self.find(MobileBy.XPATH, "//*[@text='添加成员']")
        except Exception as e:
            # 未找到则滚动到底部查找
            self.find_by_scroll("添加成员")
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.steps("./data/member.yaml", "add_member")



