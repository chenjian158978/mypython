# -*- coding:utf8 -*-

"""
Learning logging

1. http://python.jobbole.com/81666/

@author: chenjian158978@gmail.com

@date: Tue, Nov 29

@time: 11:48:54 GMT+8
"""
import unittest
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)


class TestLog(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_traceback_log(self):
        try:
            a = 1/0
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            logger.exception("dfdfdfdsasdafdjlaksdjfwejiowf")
