import smtplib
from email.mime.text import MIMEText
from email.header import Header



def send_mail():
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户/密码(登录邮箱操作)
    user = "383195937@qq.com"
    password = "xuyumngjtirscafj"
    # 发送邮箱
    sender = "383195937@qq.com"
    # 接收邮箱
    receiver = "1264046996@qq.com"
    # 发送主题
    subject = 'email by python'
    add_file = open("D:\\PythonWork\\report\\20180327 041212result.html", "r").read()
    # 编写HTML类型的邮件正文（把HTML代码写进入）
    msg = MIMEText('<html><body><a href="">百度一下</a></p></body></html>', 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    # 连接发送邮件<strong><span style="color:#ff6666;">（smtplib模块基本使用格式）</span></strong>
    # smtp = smtplib.SMTP(smtpserver,465)
    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件已发出！注意查收。")

send_mail()
print("-" * 50)