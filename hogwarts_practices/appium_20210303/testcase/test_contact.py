#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/19 18:41
# @Author  : yuwenli
import allure

from appium_20210303.testcase.test_base import TestBase

"""
联系人操作测试:包括 添加联系人,搜索联系人后编辑,删除联系人
缺点:测试用例之间存在冗余代码,需要完善
"""


class TestContact(TestBase):
    @allure.feature("联系人操作")
    class TestAddMember(TestBase):
        @allure.story("添加联系人")
        def test_add_contact_manual(self):
            contact_add_name = "测试102"
            with allure.step("手动添加联系人"):
                # 联系人数据
                add_contact_data: dict = {"name": contact_add_name, "phonenum": "13886402316", "sex": "男",
                                 "email": "222612816@qq.com",
                                 "address": "测试地址"}
                self.app.start().main().goto_contact().add_member_method().add_member_information_submit(add_contact_data)

        @allure.story("搜索后编辑联系人")
        def test_edit_contact(self):
            """
            1.进入搜索页面
            2.查找姓名 contact_search_name
            3.进入个人信息,修改 _update_data
            """
            # 搜索数据
            contact_search_name = "测试13"
            # 修改数据
            _update_data = {"name": "测试再次修改了21", "sex": "男"}
            with allure.step("进入搜索页面"):
                search = self.app.start().main().goto_contact().enter_search_contact()
            with allure.step("搜索页面搜索联系人"):
                search_data = {"name": contact_search_name}
                contact_information = search.search_contact(search_data)
            with allure.step("进入个人信息页面编辑后提交"):
                contact_information.contact_detail_setting().edit_contact(_update_data)

        # @allure.story("点击名称,删除成员测试")
        # def test_delete_contact(self):
        #     contact_name = "测试1"
        #     with allure.step("进入详细信息"):
        #         contact = self.app.start().main().goto_contact().contact_detail(contact_name)
        #     with allure.step("个人信息页面进入编辑后删除"):
        #         contact.contact_detail_setting().delete_contact()
        #
        @allure.story("搜索后删除联系人")
        def test_delete_after_search_contact(self):
            contact_search_name = "测试102"
            search_name: dict = {"name": contact_search_name}
            with allure.step("进入搜索页面"):
                search = self.app.start().main().goto_contact().enter_search_contact()
                with allure.step("搜索页面搜索联系人"):
                    contact_information = search.search_contact(search_name)
                with allure.step("进入个人信息页面删除联系人"):
                    contact_information.contact_detail_setting().delete_contact()

