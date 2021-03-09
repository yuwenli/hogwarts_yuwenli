#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/9 11:26
# @Author  : yuwenli



import allure

from appium_20210303.testcase.test_base import TestBase
@allure.feature("添加成员")
class TestAddMember(TestBase):
    @allure.story("添加成员测试")
    def test_add_member2(self):
        with allure.step("手动添加成员"):
            self.app.start().main().goto_contact().add_memeber_from_yaml_manual()