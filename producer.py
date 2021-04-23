try:
    import main
    import pika
    from rand_num_gen import randNumGen, inputNumber
except Exception as e:
    print("Some Modules are Missing {}".format(e))


if __name__ == "__main__":
    # Sending Message to Consumer
    server = main.RabbitmqConfiguration(queue='hello',
                                   host='localhost',
                                   routing_key='hello',
                                   exchange='')
    #Using the context manager
    with main.RabbitMq(server) as rabbitmq:
        rabbitmq = main.RabbitMq(server)
        payload = inputNumber(message = "Enter the size of the number  between 1 and 10 : ")
        rabbitmq.publish(payload=randNumGen(int(payload)))

    # Reciving Message From Consumer
    serverconfig = main.RabbitMqServerConfigure(host='localhost',
                                            queue='hello_2')
    server = main.rabbitmqServer(server=serverconfig)
    server.startserver()
