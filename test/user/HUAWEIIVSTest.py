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
#  -------------------华为IVS平台数据构造--------------------------

class TestHUAWEIIVS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        sql001 = "delete from `ifaas_basicinfo`.`t_third_platform_info` where id = 20000 "
        sql002 = "delete from `ifaas_basicinfo`.`t_base_platform_type` where id = 200 "
        InsertSQL2(sql001,sql002)

    def test_AgetCamera(self):
        sql1 = "INSERT INTO `ifaas_basicinfo`.`t_third_platform_info` (`id`, `type_id`, `name`, `ip`, `port`, `user_name`, `password`, `other`, `remark`, `create_time`, `update_time`, `server_id`, `engine_id`, `platform_code`, `area_id`, `vendor`) VALUES ('20000', '1', '华为IVS平台', '59.36.10.215', '9900', 'intellif01', 'Huawei@123', NULL, NULL, '2020-03-17 09:56:35', NULL, NULL, NULL, '88888888888888888888', '1', NULL);"
        sql2 = "INSERT INTO `ifaas_basicinfo`.`t_base_platform_type` (`id`, `value`, `remark`, `describle`, `create_time`, `update_time`) VALUES ('200', 'hw_ivs', NULL, NULL, '2020-03-17 09:56:35', NULL);"
        InsertSQL2(sql1, sql2)
        time.sleep(5)
        print "华为IVS平台对接系统OK，等待摄像头同步"

        time.sleep(300)
        sql3 = "SELECT * from ifaas_basicinfo.t_camera_info where manufacturer = 'HUAWEI';"
        ExecuteSQL(sql3)
        self.assertGreaterEqual(ExecuteSQL(sql3),1)

    def test_BstartTask(self):
         sql4 = "UPDATE ifaas_basicinfo.t_camera_info SET STATUS = '1' WHERE manufacturer = ‘HUAWEI’；"
         InsertSQL1(sql4)

    @classmethod
    def tearDownClass(cls):
        sql5 = "delete from `ifaas_basicinfo`.`t_third_platform_info` where id = 20000 "
        sql6 = "delete from `ifaas_basicinfo`.`t_base_platform_type` where id = 200"
        InsertSQL2(sql5,sql6)
        sql7 = "delete from ifaas_basicinfo.t_camera_info where manufacturer = 'HUAWEI'"
        InsertSQL1(sql7)
if __name__ == '__main__':
    unittest.main(verbosity=2)

