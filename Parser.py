import json

import SendMail
import editHTML


class Parser:
    sendMail = SendMail.SendMail()
    msg='' # msg = jsondata(sender, receiver, subject), HTML id,

    def setMsg(self,msg):
        self.msg=msg

    def parsing(self):
        params=self.msg.decode('utf-8')
        dictParams=json.loads(params)
        self.sendMail.setMailInfo(dictParams['htmlId'],dictParams['verifyingKey'],dictParams['sender'],dictParams['receiver'],dictParams['subject'])

        #edit html
        edit = editHTML.EditHTML()
        edit.setTemplateId(dictParams['htmlId'])
        edit.setVerifyKey(dictParams['verifyingKey'])
        edit.editHTML()

        self.sendMail.setMsg("hello")

        #send
        self.sendMail.sendMail()