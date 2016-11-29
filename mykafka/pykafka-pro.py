# -*- coding:utf8 -*-

"""
@author: chenjian158978@gmail.com

@date: Mon, Nov 21

@time: 15:21:34 GMT+8
"""
import time
from datetime import datetime

from pykafka import KafkaClient

topic = 'dnshj'
hosts = "10.0.0.156:9092,10.0.0.156:9093,10.0.0.156:9094,10.0.0.156:9095,10.0.0.156:9096"

kafka = KafkaClient(hosts=hosts)

topic = kafka.topics[topic]

producer = topic.get_sync_producer(delivery_reports=True)


for i in range(1, 9):
    now = datetime.now()
    print now
    data = '{"id": %s, "url": "http://cniil.csip.org.cn", "sitename": "国家信息无障碍公共服务平台", "firm": "ddd", "device": "设备"}' % str(i)
    producer.produce(data)
    # time.sleep(5)
    print data
    # break
# count = 0
# while True:
#     count += 1
#     producer.produce('test msg', partition_key='{}'.format(count))
#     if count % 10 ** 5 == 0:  # adjust this or bring lots of RAM ;)
#         while True:
#             try:
#                 msg, exc = producer.get_delivery_report(block=False)
#                 if exc is not None:
#                     print 'Failed to deliver msg {}: {}'.format(
#                         msg.partition_key, repr(exc))
#                 else:
#                     print 'Successfully delivered msg {}'.format(
#                         msg.partition_key)
#             except Queue.Empty:
#                 break
