import unittest

class TestCase(unittest.TestCase):

    def test_case1(self):
        print('这是第一条测试用例')

    def test_case2(self):
        print("第二条测试用例")

    @unittest.SkipTest
    def test_case3(self):
        print("使用@unittest.SkipTest 这条用例将不执行")

    def setUp(self) -> None:
        print("这是测试用例测试执行前执行")

    def tearDown(self) -> None:
        print("这是在测试用例执行完成后执行")

    @classmethod
    def setUpClass(cls) -> None:
        print('这是在测试类执行前执行')

    @classmethod
    def tearDownClass(cls) -> None:
        print('这是在测试类执行完成后执行')

    # 断言
    def test_case5(self):
        print('断言相等')
        self.assertEqual(1, 2, "判断1==2")

    def test_case6(self):
        print('断言不相等')
        self.assertNotEqual(1, 2, "判断1!=2")


class Testcase2(unittest.TestCase):
    def test_case11(self):
        print('测试类2 测试用例1')


if __name__ == '__main__':
    ##执行当前文件的所有用例
    # unittest.main()

    # #添加到测试套件里批量执行官
    # suite=unittest.TestSuite()
    # suite.addTest(TestCase('test_case2'))
    # unittest.TextTestRunner().run(suite)

    # 执行测试类或多个测试类,将测试类添加到测试套件，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Testcase2)
    suite=unittest.TestSuite([suite2,suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)
