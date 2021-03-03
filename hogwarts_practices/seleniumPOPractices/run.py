#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 12:52
# @Author  : yuwenli

import os
import shutil

import pytest

# currend_dir = os.getcwd()
path = os.path.abspath('.')
report_dir = os.path.join(path, 'report')
html_dir = os.path.join(path, 'report', 'html')

path = os.path.abspath('.')
cases_file = os.path.join(path, 'testcase').replace('\\', '/')
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
        ['-v', '-s', r'E:/lago/python_project1/hogwarts_practices/seleniumPOPractices/testcase',
         '--alluredir=E:/lago/python_project1/hogwarts_practices/seleniumPOPractices/report'
         ])
    os.system("allure generate %s -o %s --clean" % (report_dir, html_dir))
