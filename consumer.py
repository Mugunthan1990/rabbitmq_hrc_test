try:
    import main
    import pika
    import ast
    from rand_num_gen import reverseNum, inputNumber
except Exception as e:
    print("Some Modules are Missing {}".format(e))



if __name__ == "__main__":
    #Reciving Message from Producer
    serverconfig = main.RabbitMqServerConfigure(host='localhost',
                                            queue='hello')
    with main.rabbitmqServer(serverconfig) as rabbitmq:
        rabbitmq = main.rabbitmqServer(server=serverconfig)
        rabbitmq.startserver()




    #Sending message to Producer
    server = main.RabbitmqConfiguration(queue='hello_2',
                                   host='localhost',
                                   routing_key='hello_2',
                                   exchange='')
    with main.RabbitMq(server) as rabbitmq:
        rabbitmq = main.RabbitMq(server)
        payload = inputNumber(message = "Enter the number to reverse : ")
        rabbitmq.publish(payload=reverseNum(int(payload),0))
