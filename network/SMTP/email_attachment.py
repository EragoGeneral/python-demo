from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
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
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('o13.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(","), msg.as_string())
server.quit()