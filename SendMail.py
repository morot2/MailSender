import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from builtins import print, open
import codecs

##smtp assign info
smtpId = ""
smtpPassword = ""

class SendMail:
    sender = "" # email sender
    receiver = "" # email receiver
    plainText = "" # text into message
    html = "" # html into message
    verifyingKey="" ##email verifying key

    ##html template ID
    templateID=""

    msg = MIMEMultipart('alternative')

    def setSMTP(self,id,pw):
        smtpId=id
        smtpPassword=pw

    def setMailInfo(self, htmlId, verifyingKey, sender, receiver, subject):
        self.sender = sender
        self.templateID=htmlId
        self.verifyingKey=verifyingKey
        self.receiver = receiver
        self.msg['To'] = receiver
        self.msg['From'] = sender
        self.msg['Subject'] = subject
        print(subject)
        print(self.msg['Subject'])

    def setMsg(self, text):
        # attach html text into message
        htmlFile = codecs.open('./template/template'+self.templateID+'.html','r','utf-8')
        htmlStr = htmlFile.read()
        self.html = MIMEText(htmlStr, 'html')
       # self.plainText = MIMEText(text, 'plain')
       # self.msg.attach(self.plainText)
        self.msg.attach(self.html)  # htmlStr

    def sendMail(self):
        try:
            # Send the message
            s = smtplib.SMTP_SSL('smtp.naver.com', 465)
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # message to send - here it is sent as one string.
            s.login(smtpId, smtpPassword)
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
            s.quit()
            print("success")
        except smtplib.SMTPException:
            print("fail")