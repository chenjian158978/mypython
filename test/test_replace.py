# -*- coding:utf8 -*-

"""
@author: chenjian158978@gmail.com

@date: Tue, Dec 13

@time: 14:14:58 GMT+8
"""
with open("test.txt", "r") as f:
    a = f.readline()
    print a
    if a.find("\\") != -1:
        b = a.replace("\\", "")
        print b