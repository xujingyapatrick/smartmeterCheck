# -*- coding: utf8 -*-
#refreence:http://www.runoob.com/python/python-email.html
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send(msg):
    sender = 'test@localhost'
    receivers = ['xujingyastan@gmail.com']  # 接收邮件

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("Smartmeter LocalServer", 'utf-8')
    message['To'] =  Header("ESG Group", 'utf-8')

    subject = 'Local server daily report'
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "email sent successfully!"
    except smtplib.SMTPException:
        print "Error: unable to send email!"
