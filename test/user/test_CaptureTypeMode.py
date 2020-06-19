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

#  -------------------支持抓拍模式摄像头功能测试--------------------------
cameraID = 300000
cameraip = "192.168.8.100"
camerauser = "admin"
camerapasswd = "introcks1234"

class TestCaptureTypeCamera(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        print "========初始化数据库========"
        DeleteCamera(cameraip)
        time.sleep(3)
    def test_AddCamera(self):
        AddCamera(cameraID, cameraip, camerauser, camerapasswd)  # 添加摄像头"192.168.8.232"
        self.assertEqual( 1,SelectCamera(cameraip))  # 断言
    # #启动采集任务
    time.sleep(5)
    def test_Bstart_Task(self):
        StartTask(cameraip)
        time.sleep(180)
        SelectTask(cameraip)
        self.assertEqual(1, SelectTask(cameraip))  # 断言
    def test_Cstop_Task(self):
        StopTask(cameraip)
        time.sleep(180)
        SelectTask(cameraip)
        self.assertEqual(0, SelectTask(cameraip))  # 断言
    @classmethod
    def tearDownClass(cls):
      DeleteCamera(cameraip)
if __name__ == '__main__':
    unittest.main(verbosity=2)