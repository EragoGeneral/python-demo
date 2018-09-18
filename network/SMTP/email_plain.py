from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'lhr_nicelife@163.com' # input('From: ')
password = 'Love20160120' #input('Password: ')
to_addr =  '152668252@qq.com, 376939627@qq.com' #input('To: ')
smtp_server = 'smtp.163.com' #input('SMTP server: ')

# 普通郵件
msg = MIMEText('Hi guy', 'plain', 'utf-8')
msg['From'] = _format_addr('163邮箱木木 <%s>' % from_addr)
msg['To'] = to_addr #_format_addr('卓灼上神 <%s>' % to_addr)
msg['Subject'] = Header('测试Python的邮件', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(","), msg.as_string())
server.quit()