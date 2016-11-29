import pika

from Sender import Parser

connection = pika.adapters.blocking_connection.BlockingConnection
channel = pika.adapters.blocking_connection.BlockingChannel

class ReceiveMQ:

    queue='emailMessageQueue'

    def setQueue(self,queue):
        self.queue=queue

    def receiveMQ(self):
        global connection, channel
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)  # queue name
        # consume
        channel.basic_consume(callback,
                          queue=self.queue,
                          no_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

def callback(ch, method, properties, body):
    msg = body
    print("[x] Received %r" % msg)
    parser = Parser.Parser() # to use same instance
    parser.setMsg(msg) # insert msg = jsondata(sender, receiver, subject), HTML id,
    parser.parsing() # parse the msg