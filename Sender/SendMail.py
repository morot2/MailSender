import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from builtins import print, open
import codecs

class SendMail:
    sender = "" # email sender
    receiver = "" # email receiver
    plainText = "" # text into message
    html = "" # html into message

    ##html template ID
    templateID=""

    ##smtp assign info
    smtpId=""
    smtpPassword=""

    msg = MIMEMultipart('alternative')

    def setTemplateID(self,templeId):
        self.templateID=templeId

    def setMailInfo(self, sender, receiver, subject):
        self.sender = sender
        self.receiver = receiver
        self.msg['To'] = receiver
        self.msg['From'] = sender
        self.msg['Subject'] = subject

    def setMsg(self, text):
        # attach html text into message
        htmlFile = codecs.open('./template/template'+self.templateID+'.html','r','utf-8')
        htmlStr = htmlFile.read()
        self.html = MIMEText(htmlStr, 'html')
       # self.plainText = MIMEText(text, 'plain')
       # self.msg.attach(self.plainText)
        self.msg.attach(self.html)  # htmlStr

    def setSMTP(self,id,password):
        self.smtpId=id
        self.smtpPassword=password

    def sendMail(self):
        try:
            # Send the message
            s = smtplib.SMTP_SSL('smtp.naver.com', 465)
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # message to send - here it is sent as one string.
            s.login(self.smtpId, self.smtpPassword)
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
            s.quit()
            print("success")
        except smtplib.SMTPException:
            print("fail")
