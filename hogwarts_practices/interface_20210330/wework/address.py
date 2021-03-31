#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/30 10:24
# @Author  : yuwenli

import requests

from interface_20210330.common.base import Base

"""
封装接口类,继承基类
通讯录
"""
path = './data/contact.yml'
interface_class = "Address"


class Address(Base):

    def create_member(self, userid, name, mobile, department):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {"userid": userid,
                  "name": name,
                  "mobile": mobile,
                  "department": department
                  }
        r = self.send_contact("POST", url=create_member_url, json=data)
        return r.json()

    def get_member_infomation(self,userid):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        data = {"userid": userid,
                  }
        r = self.send_contact("GET", url=get_member_url, json=data)
        return r.json()

    def delete_member(self,userid):
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        data = {"userid": userid}
        r = self.send_contact("GET", url=delete_member_url, params=data)
        return r.json()

    def update_member(self,userid,new_name):
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {"userid": userid, "name" : new_name}
        r = self.send_contact("POST", url=delete_member_url, json=data)
        return r.json()

    # 以下方法是通过yaml解析接口参数和方法
    def create_member_yaml(self):
        # interface_class = "Address"
        interface_para = "create_member"
        r, expect = self.send(path,interface_class,interface_para)
        # print(r.json())
        return r.json(), expect

    def get_member_infomation_yaml(self):
        interface_para = "get_member"
        r, expect = self.send(path, interface_class, interface_para)
        return r.json(), expect

    def delete_member_yaml(self):
        interface_para = "delete_member"
        r,expect = self.send(path, interface_class, interface_para)
        return r.json(), expect

    def update_member_yaml(self):
        interface_para = "update_member"
        r, expect = self.send(path, interface_class, interface_para)
        return r.json(), expect
