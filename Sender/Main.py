from Sender import ReceiveMQ, SendMQ, SendMail

sendMQ = SendMQ.SendMQ()
receiveMQ = ReceiveMQ.ReceiveMQ()

class Main:

    def setSMTP(self,smtpId,smtpPassword):
        SendMail.smtpId = smtpId
        SendMail.smtpPassword=smtpPassword

    def run(self,params):
        # publish to Q
        sendMQ.setVar(params)
        sendMQ.sendMQ()

        ## ------------- set Message Queue ----------------
        # receiveMQ.setQueue(queueName)

        # subscribe from Q
        receiveMQ.receiveMQ()


