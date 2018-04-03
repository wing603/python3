import requests
from public_file import config_info
import json

class TestHttp(object):

    def __init__(self):
        self.url = config_info.url()

    def get_main(self,url,data):
        res = requests.get(url,data)
        code = res.status_code
        print(code)
        return code

    def post_main(self,url):
        res = requests.post(url)
        text = res.json()
        return text
        pass
