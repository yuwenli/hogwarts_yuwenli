#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 17:37
# @Author  : yuwenli
import allure

from appium_20210303.testcase.test_base import TestBase
@allure.feature("添加成员")
class TestAddMember(TestBase):
    @allure.story("添加成员测试")
    def test_add_member(self):
        with allure.step("手动添加成员"):
            name = "测试1"
            sex = "女"
            phonenum= '18898426312'
            email = "2225290912@qq.com"
            address = "测试地址1"
            self.app.start().main().goto_contact().add_member_manual(name,sex,phonenum,email,address)