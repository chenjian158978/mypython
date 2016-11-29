# -*- coding:utf8 -*-

"""
Learning with

with context_expression [as target(s)]:
    with-body

1. https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/


@author: chenjian158978@gmail.com

@date: Tue, Nov 29

@time: 10:54:40 GMT+8
"""
import unittest


class TestWith(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_openfile(self):
        with open("with.log") as file_open:
            for line in file_open:
                print line

    def test_dummyresource(self):
        # with DummyResource('Normal'):
        #     print '[with-body] Run without exceptions.'

        with DummyResource('With-Exception'):
            print '[with-body] Run with exception.'
            raise Exception
            print '[with-body] Run with exception. Failed to finish statement-body!'

    def test_contextlib(self):
        from contextlib import contextmanager

        @contextmanager
        def demo():
            print '[Allocate resources]'
            print 'Code before yield-statement executes in __enter__'
            yield '*** contextmanager demo ***'
            print 'Code after yield-statement executes in __exit__'
            print '[Free resources]'

        with demo() as value:
            print 'Assigned Value: %s' % value


class DummyResource:
    def __init__(self, tag):
        """

        :type tag: String
        """
        self.tag = tag
        print 'Resource [%s]' % tag

    def __enter__(self):
        """

        :type self: object
        """
        print '[Enter %s]: Allocate resource.' % self.tag
        return self	  # 可以返回不同的对象

    def __exit__(self, exc_type, exc_value, exc_tb):
        """

        :type exc_type: object
        """
        print '[Exit %s]: Free resource.' % self.tag
        if exc_tb is None:
            print '[Exit %s]: Exited without exception.' % self.tag
        else:
            print '[Exit %s]: Exited with exception raised.' % self.tag
            return False   # 可以省略，缺省的None也是被看做是False