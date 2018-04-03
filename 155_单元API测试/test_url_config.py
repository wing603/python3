import requests
import unittest
import json
from public_file import base_info
from public_file import Get_Post_info
class TestUrlCconfig(unittest.TestCase):

    def setUp(self):

        method = "get"
        self.url = base_info.get_url(method)

    def tearDown(self):
        pass

    def test_a1(self):
        data = {"username":"123",
                "password":"123456"}
        r = Get_Post_info.TestHttp().get_main(self.url,data)
        self.assertEquals(r,200)

    def test_a2(self):
        pass




