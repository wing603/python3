# -*- coding:utf-8 -*-
# 批量用例执行--手工加载


import requests
import json
import unittest
import time, os
import HTMLTestRunner


class MyTest(unittest.TestCase):
    def setUp(self):
        print("start test")
        self.url = "https://test1-impression.fishsaying.com/bai/project/test/"
        pass

    def tearDown(self):
        print("end test")
        pass

    def test_post_api(self):
        # case1
        post_data = {"user": 123,
                     "passwprd": 123,
                     "pay_account": 123}
        r = requests.post(url=self.url, data=post_data)
        r_dict = json.loads(r.text)
        r_code = r_dict["code"]
        self.assertEqual(r_code, 200, msg="请求通过")
        print(r.headers)
        # print(r.text)
        # print(r.status_code)

    def test_post_api_2(self):
        post_data = {"user": "wangjin",
                     "passwprd": 123,
                     "pay_account": 123}
        r = requests.post(url=self.url, data=post_data)
        r_dict = json.loads(r.text)
        r_code = r_dict["code"]
        self.assertEquals(r_code, 403, msg="请求失败")

    def test_post_api_3(self):
        post_data = {"user": "",
                     "passwprd": "",
                     "pay_account": ""}
        r = requests.post(url=self.url, data=post_data)
        t = r.text
        s = json.loads(t)
        r_dict = s
        r_code = r_dict["code"]
        self.assertEquals(r_code, 500, msg="请求失败")


def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(MyTest("test_post_api"))
    # suiteTest.addTest(MyTest("test_post_api_2"))
    return suiteTest
#
#
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite())
      # unittest.main()
#     # 执行测试
#     # suite = unittest.TestSuite()
#     # suite.addTest(MyTest("test_post_api"))
#     # suit.addTest(MyTest("test_post_api_2"))
#     # file_path = "D:\\report.html"
#     # fp = file(file_path, "wb")
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'我是测试报告的标题'
#     #                                        , description=u'我是测试报告的描述')

#     # print("success case:")
#     # print("fail case:")
#     # fp.close()
