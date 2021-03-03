#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 11:38
# @Author  : yuwenli
import allure

from seleniumPOPractices.page.main_page import MainPage

"""
添加成员测试用例
"""
@allure.feature("添加成员")
class TestContact:
    def setup(self):
        self.main_page = MainPage()

    @allure.story("添加成员测试用例")
    def test_add_member(self, get_datas_member):
        # 添加成员
        print(get_datas_member)
        with allure.step("添加成员"):
            page = self.main_page.goto_add_member()
            page.add_member(get_datas_member[0], get_datas_member[1], get_datas_member[2])
            names = page.get_member()
            assert get_datas_member[0] in names