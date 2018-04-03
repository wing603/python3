import requests
import json
import unittest


class TestTwo(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.baidu.com"
        # self.method = "get"
        # self.url = ''.join([self.host, self.method])

    def test_1(self):
        r = requests.get(url=self.url)
        r.status_code
        print(r.status_code)
        self.assertEquals(r.status_code, 300)

    def test_2(self):
        r = requests.get(url=self.url)
        r.status_code
        self.assertEquals(r.status_code, 200)

    def tearDown(self):
        pass
