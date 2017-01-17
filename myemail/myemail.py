# -*- coding:utf8 -*-

"""
该功能配合Alfred的workfolw完成：
1. 写入excel
2. 发送邮件

@author: chenjian158978@gmail.com

@date: Sat, Jan 14

@time: 10:35:56 GMT+8
"""

import sys
query = sys.argv[1]

query_list = query.split()

raw_one = query_list[0]
raw_two = query_list[1]
raw_three = query_list[2] if len(query_list) is 3 else None

import os.path
from datetime import datetime

import xlrd
from xlutils.copy import copy
import smtplib

import email
from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import mimetypes


From = "xxxxx@xxxxx.com"
To = "xxxxx@xxxxx.com"
FILE_PATH = "/Users/jianchan/Documents/qgs/xxxx.xls"
SUBJECT = "工作日志-xxxx"


class QGSSendEmail(object):
    @staticmethod
    def delta_days():
        """ 已知初始日期的行数，算出今日需要填写的行数

        :return: 今天所需的行数
        """
        today = datetime.today()
        begin_day = datetime(2016, 10, 20)
        day_delta = (today - begin_day).days
        return 4 + day_delta

    def write_excel(self):
        """ 写入excel

        :return:
        """
        try:
            raw_num = self.delta_days()

            data = xlrd.open_workbook(FILE_PATH, formatting_info=True)
            new_data = copy(data)
            sheet = new_data.get_sheet(0)

            sheet.write(raw_num, 1, raw_one.decode('utf-8'))
            sheet.write(raw_num, 2, raw_two.decode('utf-8'))
            if raw_three:
                sheet.write(raw_num, 3, raw_three.decode('utf-8'))

            new_data.save(FILE_PATH)
        except Exception as e:
            print 'test_write_excel:' + str(e)

    @staticmethod
    def send_email():
        """ 发送邮件

        :return:
        """
        server = smtplib.SMTP("smtp.ym.163.com")
        # 仅smtp服务器需要验证时
        server.login("xxxxxxxxx@xxxxx.com", "xxxx")

        # 构造MIMEMultipart对象做为根容器
        main_msg = MIMEMultipart()

        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        # text_msg = MIMEText("我this is a test text to text mime", _charset="utf-8")
        # main_msg.attach(text_msg)

        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        ctype, encoding = mimetypes.guess_type(FILE_PATH)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        file_msg = MIMEImage(open(FILE_PATH, 'rb').read(), subtype)
        print ctype, encoding

        # 设置附件头
        basename = os.path.basename(FILE_PATH)
        # 修改邮件头
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
        main_msg.attach(file_msg)

        # 设置根容器属性
        main_msg['From'] = From
        main_msg['To'] = To
        main_msg['Subject'] = SUBJECT
        main_msg['Date'] = email.Utils.formatdate()

        # 得到格式化后的完整文本
        full_text = main_msg.as_string()

        # 用smtp发送邮件
        try:
            server.sendmail(From, To, full_text)
        finally:
            server.quit()

if __name__ == '__main__':
    QGSSendEmail().write_excel()
    QGSSendEmail().send_email()
