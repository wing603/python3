import time, os
import sys
import unittest
from HTMLTestRunner import HTMLTestRunner     #引入HTMLTestRunner模板
if __name__=="__main__":
    sys.path.append("./test_cases")
    test_dir = "./test_cases"       #指定当前文件夹下的Interface目录
    file = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py",top_level_dir=None)    #匹配开头为test的py文件

    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))    # 取当前时间
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))       # 获取当前运行的.py文件所在的绝对路径
    filename = public_path + "\\test_Report\\" + now + "report.html"   #保存的报告路径和名称
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title=u"接口自动化报告",
                            description=u"详细描述如下："
                            )
    runner.run(file)     #执行测试套件
    fp.close()