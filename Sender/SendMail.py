import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from builtins import print, open
import codecs

class SendMail:
    sender = ""
    receiver = ""
    plainText = ""
    html = ""

    ##html template ID
    templateID=""

    ##smtp assign info
    smtpId=""
    smtpPassword=""

    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = receiver

    def serTemplateID(self,templeId):
        self.templateID=templeId

    def setMailInfo(self, sender, receiver, subject):
        self.sender = sender
        self.receiver = receiver
        self.msg['Subject']=subject

    def setMsg(self, text):
        htmlFile = codecs.open('./template/template'+self.templateID+'.html','r','utf-8')
        htmlStr = htmlFile.read()
        self.html = MIMEText(htmlStr, 'html')
       ##self.plainText = MIMEText(text, 'plain')
       ##self.msg.attach(self.plainText)
        self.msg.attach(self.html)  ##htmlStr

    def setSMTP(self,id,password):
        self.smtpId=id
        self.smtpPassword=password

    def sendMail(self):
        try:
            # Send the message via local SMTP server.
            s = smtplib.SMTP_SSL('smtp.naver.com', 465)
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
            s.login(self.smtpId, self.smtpPassword)
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
            s.quit()
            print("success")
        except smtplib.SMTPException:
            print("fail")
