#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 12:20
# @Author  : yuwenli
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""
    _black_list = [(By.CSS_SELECTOR, ".ww_dialog_foot>a:nth-child(2)")]

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    cookie.pop("expiry")
                # 添加cookie，add_cookie放入字典，不能放入列表（获取到的cookie是列表形式，所以遍历列表，获取到字典，通过add_cookie添加
                self.driver.add_cookie(cookie)
        else:
            self.driver = driver

            # 如果不为空，则打开base_url
        if self.base_url != '':
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)

    def find(self, locator, value):
        try:
            # print(self.driver.current_url)
            # 加入隐式等待，判断元素是否已加载，注意visibility_of_element_located里面为元组
            self.wait_for_click(10, (locator, value))
            element = self.driver.find_element(locator, value)
            return element
        except Exception as e:
            elements = self.black_elements()
            print(f"find中的：{elements}")
            if len(elements) > 0:
                elements[0].click()

    def finds(self, locator, value):
        try:
            # print(self.driver.current_url)
            self.wait_for_click(5, (locator, value))
            return self.driver.find_elements(locator, value)
        except Exception as e:
            elements = self.black_elements()
            print(f"finds中的：{elements}")
            if len(elements) > 0:
                elements[0].click()

    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def black_elements(self):
        for black in self._black_list:
            self.wait_for_click(10, black)
            elements = self.driver.find_elements(*black)
        return elements