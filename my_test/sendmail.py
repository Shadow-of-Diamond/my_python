import smtplib
from email.mime.text import MIMEText
#测试脚本通过163发送邮件

#设置服务器所需信息
mail_host = 'smtp.163.com'  # 163邮箱服务器地址
mail_user = 'xzk1072503@163.com'  # 163用户名
mail_pass = 'xzK3....'  # 密码(部分邮箱为授权码。此处即为授权码)
sender = 'xzk1072503@163.com'  # 邮件发送方邮箱地址
receivers = ['xiezhenkun@pconline.com.cn', '251845857@qq.com'] # 收件箱地址




for i in receivers:
    try:  
        #登录并发送邮件
        #设置email信息
        #邮件内容设置
        #message = MIMEText('邮件正文','plain','utf-8')
        message = MIMEText('<html><body><h1><font color="red">邮件正文</h1>', 'html', 'utf-8') #发送带格式的正文
        message['Subject'] = 'Python发邮件测试标题'  # 邮件主题
        message['From'] = sender  # 发送方信息
        message['To'] = i  # 接受方信息
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 连接到服务器
        smtpObj.login(mail_user, mail_pass)  # 登录到服务器
        smtpObj.sendmail(sender, i, message.as_string())  # 发送
        smtpObj.quit()  # 退出
        print('success send mail to ' + i)
    except smtplib.SMTPException as e:
        print('error',e) #打印错误
