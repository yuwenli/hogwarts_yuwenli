# 企业微信添加联系人
1.data目录：data.yaml中配置member数据，放在data目录

2.page：BasePage基类加入获取元素等相关方法和初始化driver，其他页面继承基类BasePage

3.testcase目录：测试用例和conftest.py（加入获取配置文件数据data.yaml）

4.report目录：allure报告

5.run.py：通过run文件进行执行测试用例，生成报告