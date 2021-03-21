#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/21 15:38
# @Author  : yuwenli
import json

import yaml

"""
common公共方法:暂时用来测试使用
"""

# with open(path, encoding='utf-8') as f:
#     case_data = yaml.safe_load(f)
#     steps = case_data[case_name]
with open("../data/data.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    steps = data['add_member']
    # print(steps)
    raw = json.dumps(steps)
    # print(type(raw))

    _params: dict = {"name": "测试添加成员1", "phonenum": "13886402323", "sex": "男", "email": "222612812@qq.com",
                    "address": "测试地址"}
    for key,value in _params.items():
        raw = raw.replace("${"+key+"}", value)
    raw = json.loads(raw)
    print(raw)