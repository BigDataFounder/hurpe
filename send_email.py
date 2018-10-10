#-*- coding:utf-8 _*-  
'''
@file : test2.py
@auther : Ma
@time : 2018/09/27
'''


import sys
reload(sys)
sys.setdefaultencoding('utf8')


import smtplib
from email.mime.text import MIMEText
from email.header import Header

#下面一行要设置成你自己的邮件服务器的地址以及用户名密码发件人信息
host,user,password,fromMail = smtpInfo
def sendMail(mailto,subject,body,format='plain'):
    if isinstance(body,unicode):
        body = str(body)
    me = ("%s<"+fromMail+">") % (Header(_mailFrom,'utf-8'),)
    msg = MIMEText(body,format,'utf-8')
    if not isinstance(subject,unicode):
        subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ','.join(mailto)  # 如果发给单个人，就不用写join
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    try:
        s = smtplib.SMTP()
        s.connect(host)
        s.login(user,password)
        s.sendmail(me, msg['To'].split(','), msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


sendMail(['***@**.com','***@**.cn'],'test测试邮件7','666',format='plain')