# -*- coding:utf8 -*-

"""
@author: chenjian158978@gmail.com

@date: Mon, Nov 21

@time: 15:21:34 GMT+8
"""
import json

from pykafka import KafkaClient

topic = "dnshj"
hosts = "10.0.0.156:9092,10.0.0.156:9093,10.0.0.156:9094,10.0.0.156:9095,10.0.0.156:9096"
zookeeper_connect = "10.0.0.156:21810,10.0.0.156:21811,10.0.0.156:21812"

kafka = KafkaClient(hosts=hosts)

topic = kafka.topics[topic]

offsets = topic.latest_available_offsets()

for partition, item in offsets.iteritems():
    print partition, item[0]

producer = topic.get_sync_producer(delivery_reports=True)

con = topic.get_balanced_consumer(
    consumer_group=topic,
    auto_commit_enable=True,
    zookeeper_connect=zookeeper_connect
)

print con.topic
print con.partitions

while True:
    msgs = con.consume(block=False)
    if msgs:
        print "msgs:   ", msgs.value
        print msgs.value



