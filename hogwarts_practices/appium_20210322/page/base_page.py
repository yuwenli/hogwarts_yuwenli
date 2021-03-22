#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 15:58
# @Author  : yuwenli
import json

import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging
import yaml


class BasePage:
    _driver: webdriver
    _params = {}
    _black_list = [(By.ID, "b_4")]
    _error_num = 0
    _max_num = 3

    def __init__(self, driver: webdriver = None):
        self._driver = driver
        self.data_path = "./data/data.yaml"

    def setup_implicity_wait(self,value):
        self._driver.implicitly_wait(value)

    # 查找单个元素
    def find(self, locator, value):
        logging.info(f"元素查找:locator={locator},value={value}" )
        self._error_num = 0
        try:
            WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located((locator, value)))
            return self._driver.find_element(locator, value)
        except Exception as e:
            # 黑名单处理
            self.setup_implicity_wait(30)
            # 如果次数大于max_num,则抛出异常
            if self._error_num > self._max_num:
                self._error_num = 0
                self.setup_implicity_wait(10)
                # 截图保存,报告显示截图
                self._driver.get_screenshot_as_file("tmp.png")
                allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
                raise e
            # 异常后增加1
            self._error_num += 1
            print(f"异常次数:{self._error_num}")
            for ele in self._black_list:
                eles = self._driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    # 关闭弹框后,仍需在页面查找元素
                    return self.find(locator, value)
            # 如果黑名单处理完后,仍然没有找到元素,则抛出异常
            self._driver.get_screenshot_as_file("tmp1.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            raise e

    # 多个元素查找时筛选元素
    def finds(self, locator, value):
        WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located((locator, value)))
        return self._driver.find_elements(locator, value)

    def find_click(self, locator):
        self.find(locator).click

    def find_by_scroll(self, text):
        # 滑动查找元素并且点击
        element = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().'f'text("{text}").instance(0));')
        element.click()

    def steps(self, path, case_name):
        with open(path, encoding='utf-8') as f:
            case_data = yaml.safe_load(f)
            steps = case_data[case_name]
            raw = json.dumps(steps)
            # 替换参数值,序列化json.dumps后替换
            for key, value in self._params.items():
                raw = raw.replace("${"+key+"}", value)
            # 进行反序列化:string转为python对象
            steps = json.loads(raw)
            for step in steps:
                if "by" in step.keys():
                    if step["method"] == "find_element":
                        element = self.find(step["by"], step["locator"])
                    if step["method"] == "find_elements":
                        elements = self.finds(step["by"], step["locator"])
                        index = step["index"]
                        element = elements[index]
                if step["action"] == "click":
                    element.click()
                if step["action"] == "send_keys":
                    element.send_keys(step["content"])
                if step["action"] == "None":
                    return element

