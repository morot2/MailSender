import pika

class SendMQ:

    params = "" # json data
    msg=""

    def setVar(self, params):
        self.params=params
        self.msg = params

    def sendMQ(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='emailMessageQueue')
        channel.basic_publish(exchange='',
                      routing_key='emailMessageQueue', # route to test queue
                      body=self.msg)
        print(" [x] Sent %r" % self.msg)
        connection.close()