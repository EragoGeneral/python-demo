#!/usr/bin/python
# -*- coding: UTF-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.application import MIMEApplication
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'lhr_nicelife@163.com' # input('From: ')
password = 'Love20160120' #input('Password: ')
to_addr =  '152668252@qq.com, 376939627@qq.com' #input('To: ')
cc_addr = 'linhanrui2006@163.com, henry.lin@ubtrobot.com'
smtp_server = 'smtp.163.com' #input('SMTP server: ')


# 邮件对象:
msg = MIMEMultipart()

msg['From'] = _format_addr('163邮箱木木 <%s>' % from_addr)
msg['To'] = to_addr #_format_addr('卓灼上神 <%s>' % to_addr)
msg['Subject'] = Header('测试Python的邮件', 'utf-8').encode()

# 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
   # '<p><img src="cid:0" ></p>' +
    '</body></html>', 'html', 'utf-8'))

# 首先是xlsx类型的附件
xlsxpart = MIMEApplication(open('good.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='better.xlsx')
msg.attach(xlsxpart)

# jpg类型的附件
jpgpart = MIMEApplication(open('o13.jpg', 'rb').read())
jpgpart.add_header('Content-Disposition', 'attachment', filename='new.jpg')
jpgpart.add_header('Content-ID', '<0>')
jpgpart.add_header('X-Attachment-Id', '0')
msg.attach(jpgpart)

# mp3类型的附件
mp3part = MIMEApplication(open('aa.txt', 'rb').read())
mp3part.add_header('Content-Disposition', 'attachment', filename='news.txt')
msg.attach(mp3part)

# jpg类型的附件
jpgpart1 = MIMEApplication(open('眼影新包装3.jpg', 'rb').read())
jpgpart1.add_header('Content-Disposition', 'attachment', filename='aaa.jpg')
jpgpart1.add_header('Content-ID', '<1>')
msg.attach(jpgpart1)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(","), msg.as_string())
server.quit()