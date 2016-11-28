from Sender import ReceiveMQ, SendMQ, SendMail, editHTML

sendMQ = SendMQ.SendMQ()
sendMail = SendMail.SendMail()
receiveMQ = ReceiveMQ.ReceiveMQ()
editHTML = editHTML.EditHTML()

class Main:
    verifyKey = ""
    params = ""
    templateId = ""
    smtpId=""
    smtpPassword=""

    def setSMTP(self,smtpId,smtpPassword):
        self.smtpId=smtpId
        self.smtpPassword=smtpPassword

    def setInfor(self,verifyKey,params,templateId):
        self.verifyKey=verifyKey
        self.params=params
        self.templateId=templateId

    def run(self):
        # publish to Q
        sendMQ.setVar(self.templateId, self.params)
        sendMQ.sendMQ()

        # edit html to insert verifying key
        editHTML.setTemplateId(self.templateId)
        editHTML.setVarifyKey(self.verifyKey)
        editHTML.editHTML()

        ## ------------- set Message Queue ----------------
        # receiveMQ.setQueue(queueName)

        # subscribe from Q
        parser = receiveMQ.receiveMQ()

        #send mail
        sendMail = parser.getSendMail()
        sendMail.setSMTP(self.smtpId,self.smtpPassword)
        sendMail.sendMail()