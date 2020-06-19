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
#  -------------------流媒体服务数据构造--------------------------

# 第一步插入第三方数据库信息
# 往数据库中添加NVR及摄像头相关信息
class TestMedia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
       sql00 = "delete from `ifaas_basicinfo`.`t_nvr` where id = 200"
       InsertSQL1(sql00)
       DeleteCamera("192.168.88.1")
    def test_AddCamera(self):
      sql1 = "INSERT INTO `ifaas_basicinfo`.`t_nvr` (`id`, `media_ip`, `media_port`, `user_name`, `password`, `nvr_name`, `nvr_ip`, `nvr_port`, `type`, `create_time`, `update_time`, `create_id`) VALUES ('200', '192.168.11.152', '8088', 'test', 'Introcks@123', '8830NVR', '192.168.88.30', '8000', 'hc_ipc', '2020-03-20 15:02:28', '2020-03-24 10:29:49', '1');"
      sql2 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('3000', '192.168.88.1', '8000', 'admin', 'ytlf1234', '1', '0', NULL, '', 'rtsp://admin:ytlf1234@192.168.88.1', NULL, '2020-03-17 15:56:35', '2020-03-24 10:31:08', 'POINT(34.000000 54.000000)', NULL, '1', '1', '192.168.88.114F南走道西侧', '1', '1', NULL, '[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"}]', '33', '2', '2', NULL, '00:00,24:00', '12', '200', '14d53064-5b2e-4bfd-80ab-d4192b6af224', NULL, NULL, NULL, NULL, NULL, NULL, '', '', '0', NULL, NULL);"

      # 添加NVR信息，添加与NVR对应的摄像头信息
      InsertSQL2(sql1, sql2)
      # 等待十分钟
      time.sleep(5)
      print "NVR与摄像头信息准备OK"


'''
通过如下接口链接访问并查看视频流
http://192.168.11.152:8088/api/addRTMPList?id=live33&addr=192.168.88.30&port=8000&deivce_info=33&type=hc_ipc&user=test&pwd=Introcks@123
之后在流媒体访问页面查看视频播放是否成功
'''