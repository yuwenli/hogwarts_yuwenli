import allure
import pytest
import yaml
import unittest
import os


@allure.feature("测试计算器")
class TestCalc():
    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_add(self, get_calc,get_datas_add):
        result = get_calc.add(get_datas_add[0],get_datas_add[1])
        # 判断result是浮点数，保留2位小数的处理
        if isinstance(result, float):
            # round方法处理浮点数，result保留2位小数
            result = round(result, 2)
        # 得到相加结果之后写断言
        # print(f"result:{result},expect:{expect}")
        with allure.step("计算两个数的相加和"):
            assert result == get_datas_add[2], print(f" result:{result},expect:{get_datas_add[2]}")


    @pytest.mark.run(order=2)
    # @pytest.mark.flaky(reruns=5,reruns_delay=1)
    @allure.story("测试除法")
    def test_div(self,get_calc,get_datas_div):
        with allure.step("计算两个数相除"):
            if get_datas_div[1] != 0:
                # result = self.calc.div(a, b)
                result = get_calc.div(get_datas_div[0], get_datas_div[1])
                # 判断result是浮点数，保留2位小数的处理
                if isinstance(result, float):
                    # round方法处理浮点数，result保留2位小数
                    result = round(result, 2)
                # 得到相加结果之后写断言
                # print(f"result:{result},expect: {expect}")
                assert result == get_datas_div[2], print(f" result:{result},expect:{get_datas_div[2]}")
                print("test_div")
            elif get_datas_div[1] == 0:
                # 过滤掉b=0的情况
                assert 1 == 0
                print("ZeroDivisionError")

    @pytest.mark.run(order=3)
    @allure.story("测试减法")
    def test_sub(self, get_calc, get_datas_sub):
        result = get_calc.sub(get_datas_sub[0], get_datas_sub[1])
        # 判断result是浮点数，保留2位小数的处理
        if isinstance(result, float):
            # round方法处理浮点数，result保留2位小数
            result = round(result, 2)
        # 得到相加结果之后写断言
        # print(f"result:{result},expect:{expect}")
        with allure.step("计算两个数的相减"):
            assert result == get_datas_sub[2], print(f" result:{result},expect:{get_datas_sub[2]}")

    @pytest.mark.run(order=4)
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_datas_mul):
        result = get_calc.mul(get_datas_mul[0], get_datas_mul[1])
        # 判断result是浮点数，保留2位小数的处理
        if isinstance(result, float):
            # round方法处理浮点数，result保留2位小数
            result = round(result, 2)
        # 得到相加结果之后写断言
        # print(f"result:{result},expect:{expect}")
        with allure.step("计算两个数的相乘"):
            assert result == get_datas_mul[2], print(f" result:{result},expect:{get_datas_mul[2]}")
