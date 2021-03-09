#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 16:32
# @Author  : yuwenli
import allure

from appium_20210303.page.app import App
from appium_20210303.testcase.test_base import TestBase
@allure.feature("打卡测试")
class TestDaka(TestBase):
    @allure.story("打卡测试用例")
    def test_sign(self):
        with allure.step("外出打卡"):
            page = self.app.start().main().goto_workbanch().goto_daka()
            page.sign_outplace()
            text = page.get_sign_outplace()
            assert text == "外出打卡成功"
