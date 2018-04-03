#!/usr/bin/env python3
# coding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

import smtplib
import unittest
import time
import os


# =============发送邮件===================================
# def sendReport(file_new):
#     with open(file_new, 'rb') as f:
#         mail_body = f.read()
#
#     msg = MIMEText(mail_body, 'html', 'utf-8')
#     msg['Subject'] = Header('自动化测试报告', 'utf-8')
#     msg['From'] = '1264046996@qq.com'  # 发件地址
#     msg['To'] = '383195937@qq.com'  # 收件人地址，多人以分号分隔
#
#     smtp = smtplib.SMTP('smtp.qq.com')
#     smtp.set_debuglevel(1)
#     smtp.login('1264046996@qq.com', '77zxbboo')  # 登录邮箱的账户和密码
#     smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
#
#     smtp.quit()
#     print('test report has send out!')
"""
123
"""
# def send_mail(file_new):
#     f = open(file_new, 'rb')
#     mail_body = f.read()
#     f.close()
#
#     msg = MIMEText(mail_body, 'html', 'utf-8')
#     msg['Subject'] = Header("自动化测试报告", 'utf-8')
#
#     smtp = smtplib.SMTP()
#     smtp.connect('smtp.live.com')  # 邮箱服务器
#     smtp.login("wj2206906091@hotmail.com", "crystal084628")  # 登录邮箱
#     smtp.sendmail("wj2206906091@hotmail.com", "1264046996@qq.com", msg.as_string())  # 发送者和接收者
#     smtp.quit()
#     print("邮件已发出！注意查收。")

# 发送邮箱服务器
def send_mail(file_new):
    smtpserver = 'smtp.qq.com'

    # 发送邮箱用户/密码(登录邮箱操作)
    user = "383195937@qq.com"
    password = "77belover"

    # 发送邮箱
    sender = "383195937@qq.com"

    # 接收邮箱
    receiver = "1264046996@qq.com"

    # 发送主题
    subject = 'email by  python'

    # 编写HTML类型的邮件正文（把HTML代码写进入）
    msg = MIMEText('<html><body><a href="">百度一下</a></p></body></html>', 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件<strong><span style="color:#ff6666;">（smtplib模块基本使用格式）</span></strong>
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


# ====================查找测试报告目录，找到最新生成的测试报告文件========
def newReport(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_dir = 'E:\\workspace\\PythonLearn1\\autoTests'  # 测试用例所在目录
    test_report = 'E:\\workspace\\PythonLearn1\\report'  # 测试报告所在目录

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_baidu*.py')

    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    filename = test_report + '\\' + now + 'result.html'  # 拼接出测试报告名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()  # 这边曾错写成fp.close，导致发送邮件时正文怎么都发不出来

    new_report = newReport(test_report)  # 获取最新报告文件
    send_mail(new_report)  # 发送最新的测试报告