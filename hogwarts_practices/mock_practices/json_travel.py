#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/23 17:32
# @Author  : yuwenli
import json

#
# def json_travel(data):
#     # 判断传入的数据类型{"a": {"b":{"c":1}}}
#     if isinstance(data, dict):
#         # 遍历字典的数据
#         # 当字典格式，递归value值
#         for key, value in data.items():
#             data[key] = json_travel(value)
#     elif isinstance(data, list):
#         # 当数据类型 为 list 的时候， 添加到结构内，并继续递归遍历，
#         # 知道数据类型不为可迭代对象时
#         data = [json_travel(value) for value in data]
#     elif isinstance(data, bool):
#         data = data
#     elif isinstance(data, int) or isinstance(data, float):
#         data = data * 1
#     elif isinstance(data, str):
#         data = data + "a"
#     else:
#         data = data
#     return data


data_test = {"data":{"items":[{"a":"test","item1":"test2"},{"a2":"test","item2":"test2"}]},"data2":"test3"}
# print(type(data_test))




def json_travel_xueqiu(data):
    items = []
    if isinstance(data, dict):
        # 遍历字典的数据
        # 当字典格式，递归value值
        for key, value in data.items():
            data[key] = json_travel_xueqiu(value)
            if key == "items":
                print(data[key])
                items.append(data[key])
            break
            # print(f'for循环里面的数据：{data[key]}')

    return items


if __name__ == '__main__':
    test = json_travel_xueqiu(data_test)
    print(test)
    # data = json.load(open("mock.json", encoding="utf-8"))
    # new_data = json_travel(data)
    # with open("mock.json", "w", encoding="utf-8") as f:
    #     json.dump(new_data, fp=f, indent=2, ensure_ascii=False)
    # new_data = json.dumps(json_travel_xueqiu(data),ensure_ascii=False)

    # print(new_data)