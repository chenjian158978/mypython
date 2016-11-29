# -*- coding:utf8 -*-

"""
@author: chenjian158978@gmail.com

@date: Mon, Nov 28

@time: 13:25:55 GMT+8
"""
from kafka import KafkaProducer

topic = 'dnshj'

bootstrap_servers = "10.0.0.156:9092,10.0.0.156:9093,10.0.0.156:9094,10.0.0.156:9095,10.0.0.156:9096"

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

print producer.partitions_for(topic)

# for i in range(1, 100):
#     producer.send(topic, 'some_message_byddddddds %s' % i)


