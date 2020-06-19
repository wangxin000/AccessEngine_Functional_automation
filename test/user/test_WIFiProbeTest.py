#! /usr/bin/python
# -*- coding:UTF-8  -*-
import time
import os
import pymysql
from lib.InsertSqlMsg import *
import unittest
import requests
import json
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入

"""
通过kafka工具查看是否有图片消息传递
"""

#----------------WiFi探针功能测试-----------------

cameraID = 50000
cameraip = "192.168.31.187"
camerauser = "admin"
camerapasswd = "ytlf1234"
# 添加的摄像头信息
class TestWIFIProbe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        print "========初始化数据库========"
        DeleteCamera(cameraip)
    # 添加的摄像头信息
    def test_Add_WIFIProbe(self):

        AddCamera(cameraID,cameraip,camerauser,camerapasswd)#添加摄像头"192.168.8.232"
        self.assertEqual( 1,SelectCamera(cameraip))  # 断言
        print "添加WIFI探针成功"
    # #启动采集任务
    time.sleep(5)
    def test_Bstart_WIFITask(self):
        StartTask(cameraip)
        time.sleep(180)
        SelectTask(cameraip)
        self.assertEqual(1, SelectTask(cameraip))  # 断言
        print "WiFi探针采集任务启动成功"

    #停止采集任务
    def test_Cstop_WIFITask(self):
        StopTask(cameraip)
        time.sleep(300)
        SelectTask(cameraip)
        self.assertEqual(0, SelectTask(cameraip))  # 断言
        print "WiFi探针任务停止成功"


   # def tearDown(self):

    @classmethod
    def tearDownClass(cls):

        print "==========tearDown======"
        DeleteCamera(cameraip)
        print "WIFI探针信息删除完毕"
if __name__ == '__main__':
    unittest.main(verbosity=2)

