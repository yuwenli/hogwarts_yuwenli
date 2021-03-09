#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 15:59
# @Author  : yuwenli
from appium import webdriver

from appium_20210303.page.base_page import BasePage
from appium_20210303.page.main_page import MainPage


class App(BasePage):

    def start(self):
        _appPackage = "com.tencent.wework"
        _appActivity = "com.tencent.wework.launch.WwMainActivity"

        if self._driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": "true",
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                "skipDeviceInitialization": True,
                "automationName": "uiautomator2",
                "autoGrantPermission":"True",
            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self._driver.start_activity(_appPackage, _appActivity)
        self._driver.implicitly_wait(5)
        return self

    def main(self):
        # 进入主页
        return MainPage(self._driver)





