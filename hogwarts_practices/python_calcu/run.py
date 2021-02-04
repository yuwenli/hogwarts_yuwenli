#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/2/4 13:36
# @Author  : yuwenli

import pytest
import os
import allure
from testcase import *

# currend_dir = os.getcwd()
path = os.path.abspath('.')
# file = currend_dir + r'\testcases\test_calcu.py'
report_dir = os.path.join(path, 'report')
html_dir = os.path.join(path, 'report', 'html')

# path = os.path.abspath('.')
# cases_file = os.path.join(path,'testcases','test_calcu.py').replace('\\','/')
# print(cases_file)
if __name__ == '__main__':
    # pytest执行某个py的类，并生成报告
    pytest.main(
        ['-v', '-s', f'E:/lago/python_project1/hogwarts_practices/python_calcu/testcases/test_caclu.py::TestCalc',
         '--alluredir=E:/lago/python_project1/hogwarts_practices/python_calcu/report'
         ])
    os.system("allure generate %s -o %s --clean" % (report_dir, html_dir))
