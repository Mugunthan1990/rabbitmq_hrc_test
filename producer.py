try:
    import pika
    from rand_num_gen import randNumGen
except Exception as e:
    print("Some Modules are Missing {}".format(e))



class MetaClass(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        " Singlton Design Pattern"
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


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
        print("Pubished Random Number : {} ".format(payload))



if __name__ == "__main__":

    server = RabbitmqConfiguration(queue='hello',
                                   host='localhost',
                                   routing_key='hello',
                                   exchange='')
    #Using the context manager
    with RabbitMq(server) as rabbitmq:
        rabbitmq = RabbitMq(server)
    payload = input("Enter the size of the number : ")
    rabbitmq.publish(payload=randNumGen(int(payload)))
