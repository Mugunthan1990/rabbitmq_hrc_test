
try:
    import pika
    from rand_num_gen import randNumGen, reverseNum
except Exception as e:
    print("Some Modules are Missing {}".format(e))


class MetaClass(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        " Singlton Design Pattern"
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

# Reciver Functions
class RabbitmqConfiguration(metaclass = MetaClass):
    def __init__(self, queue='hello', host='localhost', routing_key='hello', exchange=''):
        """ Configuration Rabbit Mq Server"""
        self.queue =  queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange


class RabbitMq():
    __slots__ = ["server", "_channel","_connection"]

    def __init__(self, server):
        """
        :param server : Object of class RabbitConfigure

        """
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))

        self._channel = self._connection.channel()
        # Declaring the Queue
        self._channel.queue_declare(queue = self.server.queue)


    # Context Manager - This will help to attomastically connect and close the server
    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self._connection.close()

    def publish(self, payload = 0):

        """
            :param payload : JSON payload
            :return: None
        """
        self._channel.basic_publish(exchange=self.server.exchange,
                     routing_key =  self.server.routing_key,
                     body = str(payload))
        print("Pubished Number : {} ".format(payload))




# Consumer Functions
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

    # Context Manager - This will help to attomastically connect and close the server
    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self._channel.close()

    @staticmethod
    def callback(ch, method, properties, body):
        payload = int(body.decode("utf-8"))
        print('Received  Number : {}'.format(payload))





    def startserver(self):
        self._channel.basic_consume(queue = self.server.queue,
                                    on_message_callback=rabbitmqServer.callback,
                                    auto_ack = True)
        try:
            self._channel.start_consuming()
        except KeyboardInterrupt:
            self._channel.stop_consuming()
            self._channel.close()
