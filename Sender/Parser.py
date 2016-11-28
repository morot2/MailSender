import json

from Sender import SendMail

class Parser:
    msg='' # msg = jsondata(sender, receiver, subject), HTML id,
    sendMail= SendMail.SendMail()

    def getSendMail(self):
        return self.sendMail

    def setMsg(self,msg):
        self.msg=msg

    def parsing(self):
        id,params=self.msg.decode('utf-8').split('-')
        dictParams=json.loads(params)
        self.sendMail.setMailInfo(dictParams['sender'],dictParams['receiver'],dictParams['subject'])
        self.sendMail.setTemplateID(id)
        self.sendMail.setMsg("hello") # not used currently