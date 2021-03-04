#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 15:58
# @Author  : yuwenli
import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver: webdriver

    def __init__(self, driver: webdriver = None):
        self._driver = driver

    def find(self, locator, value):
        WebDriverWait(self._driver,10).until(expected_conditions.visibility_of_element_located((locator,value)))
        return self._driver.find_element(locator, value)

    def finds(self, locator, value):
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located((locator, value)))
        return self._driver.find_elements(locator, value)

    # def steps(self):
    #     with open("../data/member.yaml", encoding='utf-8') as f:
    #         steps: list[dict] = yaml.safe_load(f)
    #         for step in steps:
    #             if "find_elements" in step['method']:
    #                 if "by" in step.keys

