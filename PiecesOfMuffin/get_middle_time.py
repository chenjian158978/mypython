# -*- coding:utf8 -*-

"""
该功能主要是获取两个时间段之间的某个随机时间。

1. 获取数据库中的一批数据，并进行排序；
2. 获取相邻时间段之间的某个随机时间。

@author: chenjian158978@gmail.com

@date: Fri, Dec 2

@time: 14:43:51 GMT+8
"""
import random
import datetime


import MySQLdb

MYSQL_HOST = '192.168.1.133'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_PORT = '3306'
MYSQL_DB = 'webscan'
MYSQL_CHARSET = 'utf8'


class GetMiddleTime(object):
    def __init__(self, site_id):
        self.site_id = site_id

    def get_middle_time(self):
        """获取中间的某个随机时间

        :return: 后一个状态
        """
        for first, second in self.get_data_from_sql():
            try:
                start_time = first[1]
                end_time = second[1]

                detla = start_time - end_time

                inc = random.randrange(detla.total_seconds())
                middle_time = start_time - datetime.timedelta(seconds=inc)
                # print start_time
                # print end_time
                # print middle_time
                yield end_time, middle_time
            except Exception as e:
                print str(e)

    def get_data_from_sql(self):
        """从数据库中获取数据

        :return: 第一个数据，下一个数据
        """
        try:
            result_list = []

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
                         'site_id': self.site_id}
            cursor.execute(sql)
            select_results = cursor.fetchall()
            for one in select_results:
                result_list.append(one)
            for i in range(0, len(result_list)):
                first = result_list[i]
                if i + 1 > len(result_list) - 1:
                    continue
                else:
                    second = result_list[i + 1]
                yield first, second
        except Exception as e:
            print str(e)
        finally:
            cursor.close()
            db.close()

    def update_data_from_sql(self):
        """从数据库中获取数据

        :return: 第一个数据，下一个数据
        """
        try:
            db = MySQLdb.connect(host=MYSQL_HOST,
                                 user=MYSQL_USER,
                                 passwd=MYSQL_PASSWORD,
                                 db=MYSQL_DB,
                                 charset=MYSQL_CHARSET)
            cursor = db.cursor()

            for end_time, middle_time in self.get_middle_time():
                sql = u"""UPDATE %(table_name)s
                          SET endingDate='%(ending_date)s', isClosed=2
                          WHERE websiteConfigInfo_id='%(site_id)s' AND createDate='%(create_date)s'
                      """ % {'table_name': 'websitestatus',
                             'create_date': end_time,
                             'ending_date': middle_time,
                             'site_id': self.site_id}
                print sql
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            db.rollback()
            print str(e)
        finally:
            cursor.close()
            db.close()


if __name__ == '__main__':
    for site_id in open('start.txt'):
        GetMiddleTime(site_id.replace('\n', '')).update_data_from_sql()