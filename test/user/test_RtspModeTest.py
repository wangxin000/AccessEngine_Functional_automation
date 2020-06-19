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
#  -------------------RTSP模式摄像头数据构造--------------------------

cameraip = "192.168.32.14"

# 添加的摄像头信息
class TestRtspModeCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        print "========初始化数据库========"
        DeleteCamera(cameraip)
    # 添加的摄像头信息
    def test_AddCamera(self):
        sql1 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `equipment_id`, `source_id`, `url`, `analyze_mode`, `analyze_type`) VALUES ('10058', '192.168.32.14', '8000', 'admin', 'ytlf1234', '1', '3', NULL, '', 'rtsp://admin:ytlf1234@192.168.32.126', NULL, '2020-04-17 15:55:44', '2020-05-13 21:15:29', 'POINT(34.000000 54.000000)', NULL, '1', '0', '一楼车库的摄像头14', '1', '1', NULL, '[{\"attribute\":[\"call\",\"color\",\"belt\",\"marker\",\"plate\",\"type\",\"danger\",\"brand\",\"crash\"],\"target\":\"car\"}]', '', '3', '3', NULL, '00:00,24:00', '12', '0', '3bd49fe7-0cc5-400f-baba-15d0d51fe2f9', NULL, NULL, NULL, NULL, NULL, NULL, '', '', '0', NULL, NULL, NULL, NULL, 'car');"
        InsertSQL1(sql1)
        time.sleep(10)
        self.assertEqual( 1,SelectCamera(cameraip))  # 断言
        print "添加RTSP流摄像头信息成功"
    # #启动采集任务

    def test_Bstart_Task(self):
        time.sleep(5)
        StartTask(cameraip)
        time.sleep(180)
        SelectTask(cameraip)
        self.assertEqual(1, SelectTask(cameraip))  # 断言
        print "采集任务启动成功"

    #停止采集任务
    def test_Cstop_Task(self):
        StopTask(cameraip)
        time.sleep(300)
        SelectTask(cameraip)
        self.assertEqual(0, SelectTask(cameraip))  # 断言
        print "采集任务停止成功"


   # def tearDown(self):

    @classmethod
    def tearDownClass(cls):

        print "==========tearDown======"
        DeleteCamera(cameraip)
        print "摄像头信息删除完毕"
if __name__ == '__main__':
    unittest.main(verbosity=2)

