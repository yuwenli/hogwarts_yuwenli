#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/2/13 16:12
# @Author  : yuwenli
import os

import pytest
import yaml

from python_calcu.common.calc import Calculator

path1 = os.path.abspath('.')
data_file = os.path.join(path1, 'data', 'calc.yaml').replace('\\', r'/')
with open(data_file, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['add_datas']
    div_datas = datas['div']['div_datas']
    add_myid = datas['add']['add_myid']
    div_myid = datas['div']['div_myid']
    sub_datas = datas['sub']['sub_datas']
    sub_myid = datas['sub']['sub_myid']
    mul_datas = datas['mul']['mul_datas']
    mul_myid = datas['mul']['mul_myid']


@pytest.fixture(scope="class")
def get_calc():
    calc = Calculator()
    return calc


@pytest.fixture(params=add_datas, ids=add_myid, scope="module")
def get_datas_add(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas, ids=div_myid, scope="module")
def get_datas_div(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=sub_datas, ids=sub_myid, scope="module")
def get_datas_sub(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=mul_datas, ids=mul_myid, scope="module")
def get_datas_mul(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")
