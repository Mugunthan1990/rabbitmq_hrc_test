# rabbitmq_hrc_test

This script does not contain all the aspects of the test. As I did not develop any Django or Flask  App and connect the database. I have developed the Four scripts which contain random number generators, reversing the number. and producer script will generate the random number. Consumers will receive the number and reverse it. Main will have the scripts to configure the RabbitMQ server for Producer and Consumer.

Method to running the script

- Run the consumer.py and Producer.py in separate terminal
- Then enter the size of the number that you want to generate in Producer terminal
- You will see the published random number from producer in consumer terminal
- To send reversed random number producer from consumer Press CTRL+C  consumer terminal, You will see the message to enter the number  consumer terminal. Enter the number that you want to reverse and send to producer  consumer terminal
- Finally You can see the received reversed number in  Producer terminal
