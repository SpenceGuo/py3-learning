# 如果我们本机没有 sendmail 访问，也可以使用其他服务商的 SMTP 访问（QQ、网易、Google等）

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.126.com"  # 设置服务器
mail_user = "XXXXX@126.com"  # 用户名
mail_pass = "XXXXXX"  # 口令(如果126开了授权登录，则使用授权的密码)

sender = 'hacker00001@hack.com'
receivers = ['XXXXXX@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("测试", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

