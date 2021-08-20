import allure
import pytest


# 单独运行某个模块 可以使用 pytest 【文件名】 --allure-feature【’模块名‘】
@allure.feature("登录模块")
class Testlogin():

    # 单独运行某个用力 可以使用 pytest 【文件名】 --allure-story【‘用例名’】
    @allure.story("成功登录")
    def test_login_dlcg(self):
        print('登录成功')

    @allure.story("登录失败")
    def test_login_dlsb(self):
        print('登录失败')

    @allure.story("登录步骤标记")
    def test_step(self):
        with allure.step("输入账户步骤"):
            print('输入账户')
        with allure.step("输入密码步骤"):
            print('输入密码')
        with allure.step("点击登录"):
            print('点击登录')
        assert 'a' == 1

    # 通过 allure.link('url地址',name='链接名称') 来给这个测试用力结果附加一个链接  ，可以在报告中添加这一条 用例地址 方便查看用例
    link_test = 'http://www.baidu.com'

    @allure.link(link_test, name='给链接取名')
    def test_link(self):
        print('给测试结果附加一个链接')


pytest
