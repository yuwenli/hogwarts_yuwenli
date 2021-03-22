#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 19:22
# @Author  : yuwenli
import logging
import os

import yaml


# with open("./data/data.yaml", encoding='utf-8') as f:
#     data = yaml.safe_load(f)
#     member_data = data['add_member']
#     # for step in member_data:
#     #     print(type(step))

log_dir = "./log/report.log"
# print(log_dir)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                    datefmt='%a, %d, %b %Y %H:%M:%S',
                    filename=log_dir,
                    filemode='w')
