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
#  -------------------网闸监听数据构造--------------------------





cameraID = 90000
cameraip = "192.168.7.7"
camerauser = "wangxin"
camerapasswd = "123456"
# 添加的摄像头信息
class TestNetGap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        print "========初始化数据库========"
        sql0 = "delete from `ifaas_basicinfo`.`t_trans_proxy_info`  where id = '400' "
        InsertSQL1(sql0)
        DeleteCamera("192.168.7.7")

    # 添加的摄像头信息
    def test_AddCamera(self):
        sql = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_info` (`id`, `created`, `updated`, `capability`, `name`, `password`, `port`, `station_id`, `status`, `type`, `trans_type`, `uri`, `username`, `ext1`, `ext2`, `ext3`, `is_feature`, `promote_state`, `snap_count`, `camera_count`, `netmask`, `remark`, `version`, `facility_no`, `area_id`, `engine_id`, `ip_address`) VALUES ('400', '2020-04-11 10:46:18', NULL, '0', 'NetGapTest', 'e10adc3949ba59abbe56e057f20f883e', '6666', NULL, '1', '5', '0', '192.168.6.6', 'wangxin', NULL, NULL, NULL, NULL, '0', '0', '0', NULL, NULL, NULL, NULL, '1', '20001', '192.168.6.6');"
        InsertSQL1(sql)
        print "网闸信息添加成功"

        sql2 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('90000', '192.168.7.7', '8000', 'wangxin', '123456', '1', '0', NULL, '', NULL, NULL, '2020-04-11 11:27:21', '2020-04-11 11:27:21', 'POINT(56 56)', NULL, '1', '0', 'NetGapCameraTest', '1', '1', NULL, '[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"},{\"attribute\":[\"coatPattern\",\"coatStyle\",\"gender\",\"angle\",\"bag\",\"ageStage\",\"hasCoat\",\"pantsStyle\",\"pantsPattern\",\"ride\",\"clothColor\"],\"target\":\"body\"},{\"attribute\":[\"call\",\"color\",\"belt\",\"marker\",\"plate\",\"type\",\"danger\",\"brand\",\"crash\"],\"target\":\"car\"}]', '', '2', '2', NULL, '00:00,24:00', '12', '0', '8278ffbf-b372-4f00-99c3-4ce7fe6158f0', NULL, NULL, NULL, '', NULL, NULL, '', '', '0', NULL, NULL);"
        InsertSQL1(sql2)
        self.assertEqual( 1,SelectCamera(cameraip))  # 断言
        print "添加摄像头成功"
    # 启动采集任务
        time.sleep(5)

    def test_Bstart_Task(self):
        StartTask(cameraip)
        time.sleep(180)
        SelectTask(cameraip)
        self.assertEqual(1, SelectTask(cameraip))  # 断言
        print "采集任务启动成功"

    #停止采集任务
    def test_Cstop_Task(self):
        StopTask(cameraip)
        time.sleep(180)
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
