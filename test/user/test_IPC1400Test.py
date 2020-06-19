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
#  -------------------1400协议相机数据构造--------------------------

# 第一步插入第三方数据库信息
# 往数据库中添加缓存服务器相关信息
class TestIPC1400(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        # 添加NVR信息，添加与NVR对应的摄像头信息
        sql = "delete from `ifaas_basicinfo`.`t_trans_proxy_info` where id = 666"
        sql109= "delete from `ifaas_basicinfo`.`t_camera_info` where ip = '192.168.31.65' "
        sql111 = "delete from `ifaas_basicinfo`.`t_camera_info` where ip = '192.168.31.66' "
        InsertSQL1(sql)
        InsertSQL2(sql109,sql111)
        sql01 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 1000"
        sql02 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 2000"
        InsertSQL2(sql01,sql02)

        try:
            sql1 = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_info` (`id`, `created`, `updated`, `capability`, `name`, `password`, `port`, `station_id`, `status`, `type`, `trans_type`, `uri`, `username`, `ext1`, `ext2`, `ext3`, `is_feature`, `promote_state`, `snap_count`, `camera_count`, `netmask`, `remark`, `version`, `facility_no`, `area_id`, `engine_id`, `ip_address`) VALUES ('666', '2020-03-27 16:05:47', NULL, '0', '1400代理平台', '22f92d99bb38238ff3a2c98c11978e25', '41001', NULL, '0', '6', '0', '192.168.13.210', 'admin', NULL, NULL, NULL, NULL, '0', '0', '0', NULL, NULL, NULL, NULL, '1', '20001', '192.168.13.210');"
            InsertSQL1(sql1)
            print "1400代理信息添加OK"
            # 往数据库中添加摄像头相关信息
            sql2 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `equipment_id`, `source_id`, `url`, `analyze_mode`, `analyze_type`) VALUES ('1049', '192.168.31.66', '8000', '', '', '1', '0', 'hik', '44030300000000005666', NULL, NULL, '2020-05-15 19:16:39', '2020-05-23 14:15:05', 'POINT(45.000000 45.000000)', NULL, '1', '1', '31.66-hikcamera', '1', NULL, NULL, '[{\"attribute\":[\"age\",\"gender\",\"hat\",\"glasses\",\"race\",\"mask\",\"pose\",\"landmark\",\"quality\"],\"target\":\"face\"},{\"attribute\":[\"clothColor\",\"angle\",\"ageStage\",\"coatStyle\",\"coatPattern\",\"pantsStyle\",\"pantsPattern\",\"hasCoat\",\"gender\",\"bag\",\"ride\"],\"target\":\"body\"},{\"attribute\":[\"color\",\"type\",\"brand\",\"call\",\"belt\",\"crash\",\"plate\",\"marker\",\"danger\"],\"target\":\"car\"}]', NULL, '2', '2', NULL, '00:00,24:00', '12', '0', '3bd49fe7-0cc5-400f-baba-15d0d51fe2f9', NULL, NULL, NULL, NULL, '1', '2a17efca-818c-4997-b8a6-627cf6d47f17', NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL);"
            sql3 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `equipment_id`, `source_id`, `url`, `analyze_mode`, `analyze_type`) VALUES ('915', '192.168.31.65', '8000', 'admin', 'ytlf1234', '1', '0', NULL, '44030520200331193402', NULL, NULL, '2020-05-07 19:09:48', '2020-05-12 12:23:34', 'POINT(56.000000 56.000000)', NULL, '1', '0', '31.65camera', '1', '1', NULL, '[{\"attribute\":[\"age\",\"gender\",\"hat\",\"glasses\",\"race\",\"mask\",\"pose\",\"landmark\",\"quality\"],\"target\":\"face\"},{\"attribute\":[\"clothColor\",\"angle\",\"ageStage\",\"coatStyle\",\"coatPattern\",\"pantsStyle\",\"pantsPattern\",\"hasCoat\",\"gender\",\"bag\",\"ride\"],\"target\":\"body\"},{\"attribute\":[\"color\",\"type\",\"brand\",\"call\",\"belt\",\"crash\",\"plate\",\"marker\",\"danger\"],\"target\":\"car\"}]', '', '3', '3', NULL, '00:00,24:00', '12', '0', '3bd49fe7-0cc5-400f-baba-15d0d51fe2f9', NULL, NULL, NULL, '', NULL, NULL, '', '', '0', NULL, NULL, NULL, NULL, 'face,body,car');"

            InsertSQL2(sql2, sql3)
            print "添加摄像头信息成功"

            time.sleep(5)

            # 往数据库中添加相关代理信息
            sql4 = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_topology` (`id`, `source_id`, `source_type`, `source_channel`, `proxy_id`, `ext1`) VALUES ('1000', '915', '0', '0', '666', NULL);"
            sql5 = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_topology` (`id`, `source_id`, `source_type`, `source_channel`, `proxy_id`, `ext1`) VALUES ('2000', '1049', '0', '0', '666', NULL);"
            InsertSQL2(sql4, sql5)
            print "代理与摄像头绑定关系信息OK"
            time.sleep(5)
        except Exception as f:
            DeleteCamera("192.168.31.66")
            DeleteCamera("192.168.31.65")
            sql6 = "delete from `ifaas_basicinfo`.`t_trans_proxy_info` where id = 666"
            InsertSQL1(sql6)
    def test_IPC1400camera(self):
        #启动采集任务
        StartTask("192.168.31.66")
        StartTask("192.168.31.65")
        time.sleep(180)
        self.assertEqual(1, SelectTask("192.168.31.66"))
        self.assertEqual(1, SelectTask("192.168.31.65"))

    def test_IPC1400camera(self):
        # 启动采集任务
        StopTask("192.168.31.66")
        StopTask("192.168.31.65")
        time.sleep(180)
        self.assertEqual(0, SelectTask("192.168.31.66"))
        self.assertEqual(0, SelectTask("192.168.31.65"))

    @classmethod
    def tearDownClass(cls):
        print "==========tearDown======"
        DeleteCamera("192.168.31.66")
        DeleteCamera("192.168.31.65")
        sql6 = "delete from `ifaas_basicinfo`.`t_trans_proxy_info` where id = 666"
        InsertSQL1(sql6)
        sql01 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 1000"
        sql02 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 2000"
        InsertSQL2(sql01, sql02)

if __name__ == '__main__':
    unittest.main(verbosity=2)


