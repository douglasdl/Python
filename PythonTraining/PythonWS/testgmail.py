# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

if __name__ == '__main__':
    to_addr = 'dleal@matsui.net'
    from_addr = 'fjbHoge01@gmail.com'
    mail_id = from_addr
    # 取得した16桁パスワードを入力する
    mail_pass = 'cbsfofeaxsakfnls'

    message = MIMEText('Hello')
    message['Subject'] = 'Hello Raspberry'
    message['From'] = from_addr
    message['To'] = to_addr

    sender = smtplib.SMTP_SSL('smtp.gmail.com')
    sender.login(mail_id, mail_pass)
    sender.sendmail(from_addr, to_addr, message.as_string())
    sender.quit()
