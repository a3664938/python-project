# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from get_data.get_data import GetDate
import time
class SendEmail:
    def __init__(self):
        self.get_data=GetDate()
        self.email_server=self.get_data.email_server()
        self.send_email_account=self.get_data.send_email_account()
        self.send_email_password=self.get_data.send_email_password()
        self.receive_email_account=self.get_data.receive_email_account()

    def send_email(self,content,sub):
        send_user = 'songqi' + '<' + self.send_email_account + '>'
        user_list=self.receive_email_account.split(';')
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub # 主题
        message['From'] = send_user
        message['To'] = ';'.join(user_list)
        server = smtplib.SMTP()
        server.connect(self.email_server)
        server.login(self.send_email_account, self.send_email_password)
        server.sendmail(send_user, user_list, message.as_string())
        server.close()

    def send_report(self,pass_count,fail_count):
        case_count=pass_count+fail_count
        pass_pecent=pass_count/case_count
        now_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        sub='接口自动化测试报告'
        content='%s运行结束，此次测试用例总数%s，通过率%.2f%%，失败%s个。'%(now_time,case_count,pass_pecent*100,fail_count)
        self.send_email(content,sub)

