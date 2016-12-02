# -*- coding:utf8 -*-

"""
Using confluent-kafka

1. install librdkafka

1.1 git clone https://github.com/edenhill/librdkafka.git
1.2 ./configure
1.3 make
1.4 sudo make install

2. pip install confluent-kafka

3. reboot

@author: chenjian158978@gmail.com

@date: Wed, Nov 23

@time: 11:39:30 GMT+8
"""
import unittest

from confluent_kafka import Producer
from confluent_kafka import Consumer, KafkaError, KafkaException


class TestConfluentKafka(unittest.TestCase):
    def setUp(self):
        self.broker = '10.0.0.156:9092,10.0.0.156:9093,10.0.0.156:9094,10.0.0.156:9095,10.0.0.156:9096'
        self.group_id = 'dnshj'
        self.topic_con = ['dnshj']
        self.topic_pro = 'dnshj'

    def test_producer(self):
        conf = {'bootstrap.servers': self.broker}

        p = Producer(**conf)
        some_data_source = ["chennnnnnnnnnnnnnnnnnnnnn", "jiansssssssssssssssssss", "hellossssssssssssssss",
                            "dddddddddddddddddddddddd"]
        for data in some_data_source:
            p.produce(self.topic_pro, data.encode('utf-8'))

        p.flush()

    def test_consumer(self):
        conf = {'bootstrap.servers': self.broker,
                'group.id': self.group_id,
                'default.topic.config': {'auto.offset.reset': 'smallest'}}

        c = Consumer(**conf)
        c.subscribe(self.topic_con)

        try:
            while True:
                msg = c.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print msg.topic(), msg.partition(), msg.offset()
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    print '%% %s [%d] at offset %d with key %s:\n' % (msg.topic(), msg.partition(), msg.offset(), str(msg.key()))
                    print msg.value()
        except KeyboardInterrupt:
            print '%% Aborted by user\n'

        finally:
            c.close()
