# -*- coding:utf8 -*-

"""
Learning try..except

1. http://www.pythontab.com/html/2013/pythonjichu_0204/210.html

@author: chenjian158978@gmail.com

@date: Tue, Nov 29

@time: 14:30:17 GMT+8
"""
import unittest


class TestTryExcept(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_traceback(self):
        import traceback
        try:
            a = 1/0
        except ZeroDivisionError as e:
            traceback.print_exc(str(e))

    def test_sys(self):
        import sys
        try:
            a = 1 / 0
        except ZeroDivisionError as e:
            info = sys.exc_info()
            print info[0], ":", info[1]
