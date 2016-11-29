# -*- coding:utf8 -*-

"""
@author: chenjian158978@gmail.com

@date: Mon, Nov 28

@time: 13:25:35 GMT+8
"""
from kafka import KafkaConsumer

topic = 'dns'
bootstrap_servers = "10.0.0.156:9092,10.0.0.156:9093,10.0.0.156:9094,10.0.0.156:9095,10.0.0.156:9096"

consumer = KafkaConsumer(topic,
                         group_id=topic,
                         bootstrap_servers=bootstrap_servers)

for msg in consumer:
    print msg.value
