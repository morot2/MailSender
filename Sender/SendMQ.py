import pika


class SendMQ:

    params = "" ## json data
    templateId = "" ##html template ID
    msg=""

    def setVar(self,tempId,params):
        self.templateId=tempId
        self.params=params
        self.msg = "-".join([self.templateId, self.params])

    def sendMQ(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='test')
        channel.basic_publish(exchange='',
                      routing_key='test',
                      body=self.msg)
        print(" [x] Sent %r" % self.msg)
        connection.close()