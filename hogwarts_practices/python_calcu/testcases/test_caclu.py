import pytest
import yaml
import unittest
import os
from python_calcu.common.calc import Calculator

path1 = os.path.abspath('.')
data_file = os.path.join(path1, 'data', 'calc.yaml').replace('\\', r'/')
# print(f"datafile:{data_file}")
with open(data_file, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['add_datas']
    div_datas = datas['div']['div_datas']
    add_myid = datas['add']['add_myid']
    div_myid = datas['div']['div_myid']
    # print(f"add_datas:{add_datas}")
    # print(f"add_myid:{add_myid}")


# 文件名以test_开头， 类名以Test开头， 方法名以test_开头
# 注意：测试类里一定不要加__init__()方法
class TestCalc():
    def setup_class(self):
        # 用例执行前执行(class)
        print("开始计算")
        # self.add_datas = add_datas
        # self.add_myid = add_myid
        # self.div_datas = div_datas
        # self.div_myid = div_myid
        # 实例化
        self.calc = Calculator()

    def teardown_class(self):
        # 用例执行结束后执行（class)
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=add_myid
    )
    @pytest.mark.add
    def test_add(self, a, b, expect):
        print(f"a:{a}")
        # 实例化计算器类
        # calc = Calculator()
        # 定义一个变量接收add方法的返回值
        # 调用相加方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，保留2位小数的处理
        if isinstance(result, float):
            # round方法处理浮点数，result保留2位小数
            result = round(result, 2)
        # 得到相加结果之后写断言
        # print(f"result:{result},expect:{expect}")
        assert result == expect, print(f" result:{result},expect:{expect}")

    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas, ids=div_myid
    )
    @pytest.mark.div
    def test_div(self, a, b, expect):
        if b != 0:
            result = self.calc.div(a, b)
            # 判断result是浮点数，保留2位小数的处理
            if isinstance(result, float):
                # round方法处理浮点数，result保留2位小数
                result = round(result, 2)
            # 得到相加结果之后写断言
            print(f"result:{result},expect: {expect}")
            assert result == expect
            print("test_div")
        elif b == 0:
            # 过滤掉b=0的情况
            assert 1 == 0
            print("ZeroDivisionError")

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")
