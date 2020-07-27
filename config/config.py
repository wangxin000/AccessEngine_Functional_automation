#! /usr/bin/python
# -*- coding: utf-8 -*
import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 数据库配置
db_host = '192.168.11.92'
db_port = 32000
db_user = 'root'
db_passwd = 'introcks1234'
db = 'ifaas_basicinfo'

# 邮件配置
smtp_server = 'smtp.sina.com'
smtp_user = 'test_auto@sina.com'
smtp_password = '5dad349dfdd6d58a'

sender = smtp_user  # 发件人
#receiver = 'wang.xin@intellif.com'  # 收件人
receiver = ['wang.xin@intellif.com',"peng.jidong@intellif.com","xiao.fen@intellif.com","li.zhiyuan@intellif.com","luo.zexuan@intellif.com","zhong.bin@intellif.com","engine_team@intellif.com"]  # 多人收件
subject = '接入引擎功能自动化测试报告'  # 邮件主题


#接入引擎信息
AccessEngine_ip = "192.168.11.92"
AccessEngine_port = 7788


