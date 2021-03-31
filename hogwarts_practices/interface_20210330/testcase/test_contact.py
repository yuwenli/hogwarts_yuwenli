#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/30 23:01
# @Author  : yuwenli
import allure

from interface_20210330.common.base import Base
from interface_20210330.wework.address import Address

"""
通讯录：yml文件配置接口，进行解析然后判断期望值是否和yml文件中expect相同
缺陷：yml文件中存在数据依赖
"""


@allure.feature("通讯录测试用例")
class TestContact:
    def setup(self):
        self.address = Address()
        print("start")

    @allure.story("创建成员")
    def test_create_member_1(self):
        with allure.step("判断成员是否存在"):
            r, expect = self.address.get_member_infomation_yaml()
            # 判断数据是否存在，存在则删除
            if r.get("errmsg") == "ok":
                with allure.step("成员存在则删除"):
                    self.address.delete_member_yaml()
                    with allure.step("删除成员后创建"):
                        r, expect = self.address.create_member_yaml()
                        assert r.get('errmsg', "network error") == expect
            # 数据不存在则创建
            else:
                with allure.step("成员不存在则直接创建"):
                    r, expect = self.address.create_member_yaml()
                    assert r.get('errmsg', "network error") == expect

    @allure.story("删除成员")
    def test_delete_member_yaml_1(self):
        # 数据存在则删除
        r,expect = self.address.get_member_infomation_yaml()
        if r.get("errmsg") == "ok":
            with allure.step("数据存在则删除"):
                r, expect = self.address.delete_member_yaml()
                assert r.get("errmsg") == "deleted"
        else:
            # 数据不存在则创建后删除
            with allure.step("不存在则创建后删除"):
                self.address.create_member_yaml()
                r, expect = self.address.delete_member_yaml()
                assert r.get("errmsg") == "deleted"

    @allure.story("获取成员信息")
    def test_get_member_infomation_1(self):
        with allure.step("查询数据是否存在"):
            # 数据存在则直接查询
            r, expect = self.address.get_member_infomation_yaml()
            if r.get("errmsg") == "ok":
                with allure.step("存在则直接返回查询"):
                    assert r.get("errmsg") == "ok"
            else:
                with allure.step("其他情况直接创建后查询"):
                    self.address.create_member_yaml()
                # 然后获取
                    r, expect = self.address.get_member_infomation_yaml()
                    assert r.get("errmsg") == expect

    @allure.story("更新成员信息")
    def test_update_member_1(self):
        with allure.step("查询数据是否存在"):
            # 数据存在则直接更新
            r, expect = self.address.get_member_infomation_yaml()
            if r.get("errmsg") == "ok":
                with allure.step("存在则删除后创建和更新"):
                    self.address.delete_member_yaml()
                    self.address.create_member_yaml()
                    r,expect = self.address.update_member_yaml()
                    assert r.get("errmsg") == expect
            else:
                with allure.step("不存在则创建和更新"):
                    self.address.create_member_yaml()
                    r, expect = self.address.update_member_yaml()
                    assert r.get("errmsg") == expect

