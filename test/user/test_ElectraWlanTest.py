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

#  -------------------电子围栏数据构造--------------------------
class TestElectraWlan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        print "========初始化数据库========"
        DeleteCamera("192.168.8.200")
    # 添加的摄像头信息
    def test_AddCamera(self):
       sql1 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('40000', '192.168.8.200', '23443', 'superuser', '123456', '1', '29', NULL, NULL, NULL, NULL, '2020-03-25 10:34:19', '2020-03-25 10:34:19', 'POINT(34 56)', NULL, '1', '0', '192.168.8.200', '1', '1', NULL, '[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"}]', NULL, '2', '2', NULL, '00:00,24:00', '12', '0', '14d53064-5b2e-4bfd-80ab-d4192b6af224', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '2', NULL, NULL);"
    #插入RTSP流摄像头信息
       InsertSQL1(sql1)
       time.sleep(5)
       print "添加电子围栏信息成功，下一步请配置电子围栏服务器并重启"
       self.assertEqual(1,SelectCamera("192.168.8.200"))
    def test_startTask(self):
       #启动电子围栏任务
       sql2 = "UPDATE ifaas_basicinfo.t_camera_info SET STATUS = '1' WHERE id = '40000'"
       InsertSQL1(sql2)
       SelectTask("192.168.8.200")
       self.assertEqual(1,SelectTask("192.168.8.200"))
       print "电子围栏采集任务启动成功"

    """
    通过kafka查看服务是否有消息传递
    ifaas-datainfos
    ifaas-multi-data-target

    """
    @classmethod
    def tearDownClass(cls):
       print "==========tearDown======"
       DeleteCamera("192.168.8.200")
       print "摄像头信息删除完毕"
if __name__ == '__main__':
    unittest.main(verbosity=2)