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

#  -------------------图片缓存服务器--------------------------



class TestImageCache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        # 第一步插入第三方数据库信息
        # 往数据库中添加缓存服务器相关信息
        sql10 = "delete from `ifaas_basicinfo`.`t_trans_proxy_info` where id = 20005 "
        InsertSQL1(sql10)
        DeleteCamera("192.168.88.9")
        DeleteCamera("192.168.88.10")
        sql23 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 100"
        sql33 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 200"
        InsertSQL2(sql23,sql33)

        try:
            sql1 = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_info` (`id`, `created`, `updated`, `capability`, `name`, `password`, `port`, `station_id`, `status`, `type`, `trans_type`, `uri`, `username`, `ext1`, `ext2`, `ext3`, `is_feature`, `promote_state`, `snap_count`, `camera_count`, `netmask`, `remark`, `version`, `facility_no`, `area_id`, `engine_id`, `ip_address`) VALUES ('20005', '2020-03-27 16:05:47', NULL, '0', '10缓存服务器', '22f92d99bb38238ff3a2c98c11978e25', '10097', NULL, '0', '4', '0', '192.168.2.10', 'intellif', NULL, NULL, NULL, NULL, '0', '0', '0', NULL, NULL, NULL, NULL, '1', NULL, '192.168.2.10');"
            InsertSQL1(sql1)
            # 添加NVR信息，添加与NVR对应的摄像头信息
            time.sleep(5)
            print "缓存服务器信息添加OK"

            # 往数据库中添加摄像头相关信息
            sql2 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('88192', '192.168.88.9', '8000', 'admin', 'ytlf1234', '1', '0', NULL, '', NULL, NULL, '2020-03-27 16:26:34', '2020-04-07 15:02:07', 'POINT(43.000000 43.000000)', NULL, '1', '1', '缓存测试camera1', '1', '1', NULL, '[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"}]', '', '3', '2', NULL, '00:00,24:00', '12', '0', '14d53064-5b2e-4bfd-80ab-d4192b6af224', NULL, NULL, NULL, NULL, NULL, NULL, '', '', '0', NULL, NULL);"
            sql3 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('88193', '192.168.88.10', '8000', 'admin', 'ytlf1234', '1', '0', NULL, '', NULL, NULL, '2020-03-27 16:27:35', '2020-04-07 15:04:15', 'POINT(34.000000 43.000000)', NULL, '1', '0', '缓存测试camera2', '1', '1', NULL, '[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"}]', '', '3', '2', NULL, '00:00,24:00', '12', '0', '14d53064-5b2e-4bfd-80ab-d4192b6af224', NULL, NULL, NULL, NULL, NULL, NULL, '', '', '0', NULL, NULL);"

            InsertSQL2(sql2, sql3)
            print "添加摄像头信息成功"

            time.sleep(5)

            # 往数据库中添加相关代理信息
            sql4 = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_topology` (`id`, `source_id`, `source_type`, `source_channel`, `proxy_id`, `ext1`) VALUES ('100', '88192', '0', '0', '20005', NULL);"
            sql5 = "INSERT INTO `ifaas_basicinfo`.`t_trans_proxy_topology` (`id`, `source_id`, `source_type`, `source_channel`, `proxy_id`, `ext1`) VALUES ('200', '88193', '0', '0', '20005', NULL);"
            InsertSQL2(sql4, sql5)
            print "添加代理信息OK"
            time.sleep(5)

          #  sql6 = "INSERT INTO `ifaas_collection`.`t_analyze_resource` (`id`, `source_id`, `source_url`, `source_type`, `source_name`, `source_size`, `user_id`, `create_time`, `update_time`, `resource_status`, `move_direction`, `label`, `org_id`) VALUES ('80003', '88193', '', 'hikCamera', '缓存测试camera2', '0', '1', '2020-04-07 15:21:32', '2020-04-07 15:21:32', '0', '', NULL, '1');"
           # sql7 = "INSERT INTO `ifaas_collection`.`t_analyze_resource` (`id`, `source_id`, `source_url`, `source_type`, `source_name`, `source_size`, `user_id`, `create_time`, `update_time`, `resource_status`, `move_direction`, `label`, `org_id`) VALUES ('80004', '88192', '', 'hikCamera', '缓存测试camera1', '0', '1', '2020-04-07 15:21:41', '2020-04-07 15:21:41', '0', '', NULL, '1');"

           # InsertSQL2(sql6, sql7)
           # print "添加采集解析任务OK"
          #  time.sleep(5)
        except Exception as f:
            sql10 = "delete from `ifaas_basicinfo`.`t_trans_proxy_info` where id = 20005 "
            InsertSQL1(sql10)
            DeleteCamera("192.168.88.9")
            DeleteCamera("192.168.88.10")

    def test_Astart_ImageCachecamera(self):
        sql8 = "UPDATE ifaas_basicinfo.t_camera_info set `status` = 1 where id = '88192'"
        sql9 = "UPDATE ifaas_basicinfo.t_camera_info set `status` = 1 where id = '88193'"
        InsertSQL2(sql8, sql9)
        time.sleep(300)
        self.assertEqual(1, SelectTask("192.168.88.9"))
        self.assertEqual(1, SelectTask("192.168.88.10"))

    def test_Bstop_ImageCache0camera(self):
        sql8 = "UPDATE ifaas_basicinfo.t_camera_info set `status` = 0 where id = '88192'"
        sql9 = "UPDATE ifaas_basicinfo.t_camera_info set `status` = 0 where id = '88193'"
        InsertSQL2(sql8, sql9)
        time.sleep(300)
        self.assertEqual(0, SelectTask("192.168.88.9"))
        self.assertEqual(0, SelectTask("192.168.88.10"))

    @classmethod
    def tearDownClass(cls):
        sql10 = "delete from `ifaas_basicinfo`.`t_trans_proxy_info` where id = 20005 "
        InsertSQL1(sql10)
        DeleteCamera("192.168.88.9")
        DeleteCamera("192.168.88.10")
        sql23 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 100"
        sql33 = "delete from `ifaas_basicinfo`.`t_trans_proxy_topology` where id = 200"
        InsertSQL2(sql23, sql33)
if __name__ == '__main__':
    unittest.main(verbosity=2)