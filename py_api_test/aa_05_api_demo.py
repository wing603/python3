# -*- coding:utf-8 -*-
# 批量用例执行--手工加载


import requests
import json
import unittest


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
        # r_dict = s
        r_code = s["code"]
        self.assertEquals(r_code, 500, msg="请求失败")


if __name__ == "__main__":
    # unittest.main()
    # 执行测试
    suit = unittest.TestSuite()
    suit.addTest(MyTest("test_post_api"))
    suit.addTest(MyTest("test_post_api_2"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    print("success case:")
    print("fail case:")
