import unittest
from testcases.baidu.test_001 import TestOne
import HTMLTestRunner
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
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
#     smtp = smtplib.SMTP_SSL('smtp.qq.com')
#     smtp.set_debuglevel(1)
#     smtp.login('1264046996@qq.com', '77zxbboo')  # 登录邮箱的账户和密码
#     smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
#
#     smtp.quit()
#     print('test report has send out!')
def send_mail(file_new):
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户/密码(登录邮箱操作)
    user = "383195937@qq.com"
    password = "xuyumngjtirscafj"
    # 发送邮箱
    sender = "383195937@qq.com"
    # 接收邮箱
    receiver = "1264046996@qq.com"
    # 发送主题
    subject = '接口测试报告'
    add_file = open("D:\\PythonWork\\report\\123.txt","r").read()
    att = MIMEText(add_file, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = '123.txt'"
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot.attach(att)
    send_file =open(file_new,"rb")
    mail_body = send_file.read()
    send_file.close()
    # with open(new_report,"rb") as send_file:
    #     send_file.read()
    # 编写HTML类型的邮件正文（把HTML代码写进入）
    msg = MIMEText(mail_body,'html','utf-8')
    # msg = MIMEText('<html><body><a href="">百度一下</a></p></body></html>', 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    # 连接发送邮件<strong><span style="color:#ff6666;">（smtplib模块基本使用格式）</span></strong>
    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件已发出！注意查收。")

# ====================查找测试报告目录，找到最新生成的测试报告文件========
def newReport(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    # print("1111")
    return file_new


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test_*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":


    # 用例路径
    case_path = os.path.join(os.getcwd())
    # 报告结果存放路径
    # report_path = os.path.join(os.getcwd(), "report")
    report_path = 'D:\\PythonWork\\report'
    print(case_path)
    print(report_path)

    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    # report_info = r'D:\\PythonWork\report\re.html'
    report_name = report_path + '\\' + now + 'result.html'
    file = open(report_name, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title="接口测试",
                                           description="接口测试牛皮")
    runner.run(all_case())
    file.close()
    print("aa" * 111)
    new_report = newReport(report_path)  # 获取最新报告文件
    send_mail(new_report)  # 发送最新的测试报告
