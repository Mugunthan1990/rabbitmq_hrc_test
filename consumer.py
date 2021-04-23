try:
    import pika
    import ast
    from rand_num_gen import reverseNum
except Exception as e:
    print("Some Modules are Missing {}".format(e))

class MetaClass(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):

        " Singlton Design Pattern"

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class RabbitMqServerConfigure(metaclass=MetaClass):

    def __init__(self, host='localhost',queue='hello'):

        """ Server initilization """

        self.host = host
        self.queue = queue

class rabbitmqServer():

    def __init__(self,server):
        """
        :parm server: Object of class RabbitMqServerConfigure
        """

        self.server  = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        # Declaring the Queue
        self._tem = self._channel.queue_declare(queue=self.server.queue)
        print("Server started waiting for a messages")

    @staticmethod
    def callback(ch, method, properties, body):
        payload = int(body.decode("utf-8"))
        print('Received Random Number : {}'.format(payload))
        print('Received Reversed Random Number : {}'.format(reverseNum(payload,0)))


    def startserver(self):
        self._channel.basic_consume(queue = self.server.queue,
                                    on_message_callback=rabbitmqServer.callback,
                                    auto_ack = True)
        self._channel.start_consuming()

if __name__ == "__main__":
    serverconfig = RabbitMqServerConfigure(host='localhost',
                                            queue='hello')
    server = rabbitmqServer(server=serverconfig)
    server.startserver()
