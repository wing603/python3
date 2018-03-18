import re, json, unittest


class getCase(unittest.TestCase):
    #setUp 执行用例前的初始化工作
    def setUp(self):
        print("testing start")
        self.url = "http://localhost:12306/"
        self.headers = {"content-type":"application/json"}
        self.json_data = json.dumps({"new":"QQ","old":"taobao"})
    # tesrDown 执行用力之后的辣鸡回收工作
    def tearDown(self):
        print("testing ending")
    # 测试get接口
    def test_get_case(self):
        results = re.get(self.url('gets')).json()
        self.assertEqual(len(results), 2)

        self.assertEqual(results[0]['title'], 'java')
        self.assertEqual(results[0]['version'], '1.8.0')

        self.assertEqual(results[1]['title'], 'python')
        self.assertEqual(results[1]['version'], '3.5')

            # 测试post接口

    def test_post_case(self):
        results = re.post(self.url('posts'), data=self.json_data, headers=self.headers)
        re = results.json()
        self.assertEqual(results.status_code, 200)
        self.assertEqual(len(re), 2)

        self.assertEqual(re[0]['fruit'], 'apple')
        self.assertEqual(re[0]['computer'], 'lenvo')

        self.assertEqual(re[1]['mobile'], 'iphone')
        self.assertEqual(re[1]['book'], 'testing')

            # 测试put接口

    def test_edit_case(self):
        results = re.put(self.url('edit'), data=self.json_data, headers=self.headers)
        re = results.json()
        self.assertEqual(results.status_code, 200)
        self.assertEqual(re['success'], 'true')

            # 测试delete接口

    def test_delete_case(self):
        results = re.delete(self.url('delete'))
        re = results.json()
        self.assertEqual(results.status_code, 200)
        self.assertEqual(re['success'], 'true')

    def url(self, path):
        return self.demian + path

    if __name__ == '__main__':
        unittest.main()