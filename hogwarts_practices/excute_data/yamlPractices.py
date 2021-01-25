#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/25 14:43
# @Author  : yuwenli

"""
5.1版本之后就修改了需要指定Loader，通过默认加载​​器（FullLoader）禁止执行任意函数，该load函数也变得更加安全
读取yaml内容 转化yaml数据为字典或列表
yaml.load(file,Loader=yaml.FullLoader)
# 支持格式嵌套
格式：
    name: xiaohong
    age: 24
    books:
      - 呐喊
      - 朝花夕拾
字典格式：
1.字典嵌套
nb1:
    user: 测试
    psw: 123456
2.单纯的字典类型
user:测试
psw: 123456

3.list序列格式
yaml里面写一个数组，前面加一个‘-’符号
- admin1: 123456
- admin2: 111111
- admin3: 222222

对应的python:
[{'admin1': 123456},
{'admin2': 111111},
{'admin3': 222222}]

4.str
n1: 12.30
n2: true
n3: false
# None用~ 表示
n4: ~
date1: 2017-07-31
# 数据类型转换（使用2个！！)
# int转str
n6: !!str 123
# bool值转str
n7: !!str true

举例说明：
n1: 12.30
n2: true
n3: false
n4: ~
time1: 2018-04-18t21:59:43.10+08:00
date1: 2018-04-18
n6: !!str 123
n7: !!str true

python读取结果：

{'n1': 12.3,
'n2': True,
'n3': False,
'n4': None,
'time1': datetime.datetime(2018, 4, 18, 13, 59, 43, 100000),
'date1': datetime.date(2018, 4, 18),
'n6': '123',
'n7': 'true'}

list+dict

- user: admin1
  psw: '123456'

dict+list
nub1:
    - admin1
    - '123456'

{'nub1': ['admin1', '123456']}

写入yaml

"""

import yaml
import os

# 打开文件，读取文件内容，关闭文件
stream = open("yamltest.yaml", mode='r+', encoding='utf-8')
# 读取yaml文件
# yaml.load 转化yaml数据为字典或列表
data_read = yaml.load(open("yamltest.yaml", mode='r', encoding='utf-8'), Loader=yaml.FullLoader)
print(data_read)  # 返回值 {'staging': 'test1'}
print(data_read.get("staging"))  # 返回value
# print(yaml.load(stream, Loader = yaml.FullLoader))
# 关闭文件

# load_all()方法返回迭代器对象
data = yaml.load_all(stream, Loader=yaml.FullLoader)
print(type(data))  # generator

for i in data:
    print(i)
    print(i.keys(), i.values())

# 使用dump()方法将一个python对象生成为yaml格式的数据
# 将python对象生成yaml格式数据，写入到yaml中
data1 = {'n1': 12.3,
         'n2': True,
         'n3': False,
         'n4': None,
         'n6': '123',
         'n7': 'true'}
# 写入数据，allow_unicode=True避免乱码
current_dir = os.getcwd()
conf_dir = os.path.join(current_dir, 'excute_data')
print(current_dir)
file_path = current_dir + r"\yamltest.yaml"
print(file_path)
if os.path.exists(file_path):
    yaml_file = open(file_path, "a+", encoding='utf-8')
    data_yaml = yaml.dump(data1, yaml_file, allow_unicode=True)
    print(data_yaml)
    # print(data_yaml.get("n2"))
# data_yaml = yaml.dump(data1,stream,allow_unicode=True)
# print(data_yaml)

stream.close()
