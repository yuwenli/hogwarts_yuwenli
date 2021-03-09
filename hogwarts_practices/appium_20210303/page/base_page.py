#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 15:58
# @Author  : yuwenli
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver: webdriver

    def __init__(self, driver: webdriver = None):
        self._driver = driver

    # 查找单个元素
    def find(self, locator, value):
        WebDriverWait(self._driver,10).until(expected_conditions.visibility_of_element_located((locator,value)))
        return self._driver.find_element(locator, value)

    # 多个元素查找时筛选元素
    def finds(self, locator, value):
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located((locator, value)))
        return self._driver.find_elements(locator, value)

    def find_click(self,locator):
        self.find(locator).click

    def find_by_scroll(self, text):
        # 滑动查找元素
        element = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().'f'text("{text}").instance(0));')
        element.click()

    def steps(self, path, case_name):
        with open(path, encoding='utf-8') as f:
            case_data = yaml.safe_load(f)
            steps = case_data[case_name]
            print(f"steps:{steps}")
            for step in steps:
                if "by" in step.keys():
                    if step["method"] == "find_element":
                        # print(step["elementName"])
                        element = self.find(step["by"], step["locator"])
                    if step["method"] == "find_elements":
                        # print(step["elementName"])
                        elements = self.finds(step["by"], step["locator"])
                        index = step["index"]
                        element = elements[index]
                if step["action"] == "click":
                    element.click()
                if step["action"] == "send_keys":
                    element.send_keys(step["content"])
                if step["action"] == "None":
                    return element

