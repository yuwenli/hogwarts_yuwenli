#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 19:22
# @Author  : yuwenli
import yaml

with open("../data/member.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    member_data = data['add_member']
    for step in member_data:
        print(type(step))
    # for member in member_data:
    #     member_element = member['elementName']
    #     member_element = member['action']
    #     if member_element == 'send_keys':
    #     print(member_element)