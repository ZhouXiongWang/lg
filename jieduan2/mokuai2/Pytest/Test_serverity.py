import allure

# 给测试用例进行用例级别标记
import pytest


class TestSeverity():
    # trivial 级别 ：轻微缺陷（必输项无提示，或提示不规范）
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_trivial(self):
        print('123')

    # Normal 级别： 普通缺陷（数值计算错误）
    @allure.severity(allure.severity_level.NORMAL)
    def test_trivial4(self):
        print('123')

    # minor 级别： 次要缺陷（界面错误，ui错误）
    @allure.severity(allure.severity_level.MINOR)
    def test_trivial3(self):
        print('123')

    # critial 级别： 临界缺陷 （功能点缺失）
    @allure.severity(allure.severity_level.CRITICAL)
    def test_trivial2(self):
        print('123')

    # blocker 级别  终端缺陷（客户端无响应）
    @allure.severity(allure.severity_level.BLOCKER)
    def test_trivial1(self):
        print('123')

# 好像不需要使用 allure.servityy_level方法 ， 可直接str复制
# 按照用例级别执行测试用例方法
# pytest  文件名 --allure[output路径]--allure-severities normal，critical,[严重级别]
# if __name__ == '__main__':
#     pytest.main()
pytest