#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/2/4 13:36
# @Author  : yuwenli

import pytest
import os
import allure
from testcase import *
import shutil

# currend_dir = os.getcwd()
path = os.path.abspath('.')
# file = currend_dir + r'\testcases\test_calcu.py'
report_dir = os.path.join(path, 'report')
html_dir = os.path.join(path, 'report', 'html')

path = os.path.abspath('.')
cases_file = os.path.join(path, 'testcases', 'test_calcu.py').replace('\\', '/')
print(cases_file)


# 删除已生成的report文件（多次运行时产生文件）
def delete_report():
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
    else:
        print("无report")


if __name__ == '__main__':
    delete_report()
    # pytest执行某个py的类，并生成报告
    pytest.main(
        ['-v', '-s', r'E:/lago/python_project1/hogwarts_practices/python_calcu2/testcases/test_caclu2.py::TestCalc',
         '--alluredir=E:/lago/python_project1/hogwarts_practices/python_calcu2/report'
         ])
    os.system("allure generate %s -o %s --clean" % (report_dir, html_dir))
