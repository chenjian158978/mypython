# -*- coding:utf8 -*-

"""
该功能主要是获取两个时间段之间的某个随机时间。

1. 获取数据库中的一批数据，并进行排序；
2. 获取相邻时间段之间的某个随机时间。

@author: chenjian158978@gmail.com

@date: Fri, Dec 2

@time: 13:37:58 GMT+8
"""
import unittest
import time
import random
import datetime

import MySQLdb

MYSQL_HOST = '192.168.1.133'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_PORT = '3306'
MYSQL_DB = 'webscan'
MYSQL_CHARSET = 'utf8'


class TestGetMiddleTime(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_middle_time(self):
        now = datetime.datetime.now()
        start_time = now
        print start_time
        days = random.randint(0, start_time.year * 365)
        print days
        seconds = random.randint(0, 60)
        print seconds
        minutes = random.randint(0, 60)
        print minutes
        hours = random.randint(0, 24)
        print hours
        end_time = start_time - datetime.timedelta(days=days, seconds=seconds, minutes=minutes, hours=hours)
        print end_time

        detla = start_time - end_time
        print detla
        print detla.total_seconds()

        inc = random.randrange(detla.total_seconds())
        result = start_time - datetime.timedelta(seconds=inc)
        print result.strftime("%Y-%m-%d %H:%M:%S")

    def test_get_time(self):
        try:
            result_list = []
            result = {'id': "",
                      'time': ""}

            db = MySQLdb.connect(host=MYSQL_HOST,
                                 user=MYSQL_USER,
                                 passwd=MYSQL_PASSWORD,
                                 db=MYSQL_DB,
                                 charset=MYSQL_CHARSET)
            cursor = db.cursor()
            sql = u"""SELECT id, createDate
                      FROM %(table_name)s
                      WHERE isClosed=0 AND websiteConfigInfo_id='%(site_id)s'
                      ORDER BY createDate DESC
                  """ % {'table_name': 'websitestatus',
                         'site_id': '40288a6c510fcbe90151145d7ceb4baf'}
            print sql
            cursor.execute(sql)
            select_results = cursor.fetchall()
            print select_results
            for one in select_results:
                result_list.append(one)
            if len(result_list) % 2 != 0:
                result_list.remove(result_list[-1])
            print len(result_list)
            for i in range(0, len(result_list))[::2]:
                first = result_list[i]
                second = result_list[i + 1]
                print first, second
        except Exception as e:
            print str(e)
        finally:
            cursor.close()
            db.close()


