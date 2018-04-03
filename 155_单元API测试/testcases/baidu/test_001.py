#! -*- coding : utf-8 -*-

import requests
import unittest
import json
import os
import time
import HTMLTestRunner


class TestOne(unittest.TestCase):

    def setUp(self):
        self.host = "http://www.httpbin.org/"
        self.method = "get"
        self.url = ''.join([self.host, self.method])


    def test_a(self):
        r = requests.get(url=self.url)
        r.headers
        t = json.loads(r.text)
        # print(t)
        # print(r.headers)
        self.assertEquals(r.headers["Connection"], "keep-alive")


    def test_b(self):
        r = requests.get(url=self.url)
        r.headers
        t = json.loads(r.text)
        # print(t)
        # print(r.headers)
        self.assertEquals(r.headers["Connection"], "keep-alive1")

    def tearDown(self):
        pass


if __name__ == '__main__':
    # unittest.main()
    print("开始main")

    suite = unittest.TestSuite()
    suite.addTest(TestOne("test_a"))
    suite.addTest(TestOne("test_b"))
    runner = unittest.TextTestRunner()
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # Report_Path = os.path("result_" + now + ".html")
    report_path = "D:\\testresult.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告如下:',
                                           description=u'用例执行情况：')

    runner.run(suite)
    fp.close()
    pass
