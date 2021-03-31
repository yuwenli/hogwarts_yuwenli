#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/30 10:36
# @Author  : yuwenli
import logging
import random

import pytest
import requests

"""
通讯录测试用例--直播课程练习
"""
from interface_20210330.wework.address import Address


class TestAddress:
    def setup(self):
        # 进行实例化和数据初始化
        self.address = Address()
        self.name = "测试" + str(random.randint(1,40))
        self.department = [2]
        # self.user_id = "test" + str(random.randint(1,40))
        self.user_id = "".join(random.choice("0123456789") for j in range(4))
        self.mobile = "138"+"".join(random.choice("0123456789") for j in range(8))

    # @pytest.mark.parametrize("user_id, mobile", [("zhangsan00123", "13812301022")])
    # 创建成员
    def test_create_member(self):
        # 判断数据是否存在，存在则删除
        r = self.address.get_member_infomation(self.user_id)
        if r.get("errmsg") == "ok":
            self.address.delete_member(self.user_id)
            r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
            assert r.get('errmsg', "network error") == "created"
        elif "userid existed" in r.get("errmsg"):
            r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
            assert r.get('errmsg', "network error") == "created"

    # 删除成员
    def test_delete(self):
        # 数据存在则删除
        r = self.address.get_member_infomation(self.user_id)
        if r.get("errmsg") == "ok":
            r = self.address.delete_member(self.user_id)
            assert r.get("errmsg") == "deleted"
        else:
            # 数据不存在则创建后删除
            r1 = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
            r = self.address.delete_member(self.user_id)
            assert r.get("errmsg") == "deleted"

    # 获取成员信息-不存在则创建后获取；存在则直接获取
    def test_get_member(self):
        r = self.address.get_member_infomation(self.user_id)
        if r.get("errmsg") == "ok":
            assert 1 == 1
        elif "userid existed" in r.get("errmsg"):
            self.address.create_member(self.user_id, self.name, self.mobile, self.department)
            r = self.address.get_member_infomation(self.user_id)
            assert r.get("errmsg") == "ok"
            assert r.get("name") == self.name

    # 更新成员姓名
    def test_update_member(self):
        new_name = "test更新名称"
        # 进行数据清洗
        r = self.address.get_member_infomation(self.user_id)
        # 根据id查看是否存在，存在则直接更新
        if r.get("errmsg") == "ok":
            r = self.address.update_member(self.user_id,new_name)
            assert r.get("errmsg") == "updated"
        # 不存在则进行创建然后更新
        else:
            r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
            assert r.get('errmsg', "network error") == "created"
            r = self.address.update_member(self.user_id,new_name)
            assert r.get("errmsg") == "updated"

