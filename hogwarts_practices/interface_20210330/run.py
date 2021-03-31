#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/30 16:07
# @Author  : yuwenli
import os
import shutil

import pytest
import xdist
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

    # pytest执行某个py的类，并生成报告
    pytest.main(
        ['-v', '-s', '-n 2',r'E:/lago/python_project1/hogwarts_practices/interface_20210330/testcase',
         '--alluredir=E:/lago/python_project1/hogwarts_practices/interface_20210330/report'
         ])
    os.system("allure generate %s -o %s --clean" % (report_dir, html_dir))