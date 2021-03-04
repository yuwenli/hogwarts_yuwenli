#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 17:38
# @Author  : yuwenli
from appium.webdriver.common.mobileby import MobileBy

from appium_20210303.page.base_page import BasePage


class MemberPage(BasePage):

    # 手动输入添加
    def add_member_manual(self,name,sex,phonenum,email,address):
        # 点击添加成员，进入添加成员页面
        try:
            # 先在页面查找“添加成员”
            element = self.find(MobileBy.XPATH, "//*[@text='添加成员']")
        except Exception as e:
            # 未找到则滚动到底部查找
            element = self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));')
        element.click()
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        self.find(MobileBy.XPATH, "//*[@text='必填']").send_keys(name)
        # 选择性别
        self.finds(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/av2']")[0].click()
        self.find(MobileBy.XPATH, f"//*[@text='{sex}']").click()
        # 输入手机号
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        # 输入邮箱
        email_elements = self.finds(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/au0']")[1]
        email_elements.send_keys(email)
        # 输入地址
        elements = self.finds(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/aut']")[1].click()
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gz']").send_keys(address)
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        # 点击保存
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()



