#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 13:10
# @Author  : yuwenli
import pytest
import yaml

filepath = "./data/data.yaml"
with open(filepath, encoding='utf-8')as f:
    data = yaml.safe_load(f)
    member_data = data['member']
    print(member_data)


@pytest.fixture(params=member_data, scope="module")
def get_datas_member(request):
    print("开始获取成员数据")
    data = request.param
    yield data
    print("结束获取成员数据")