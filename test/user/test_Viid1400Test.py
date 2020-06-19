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

#  -------------------viid1400视图库功能测试-------------------------


class TestViid1400Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        print "预置平台类型信息"
        sql0 = "delete from `ifaas_basicinfo`.`t_base_platform_type` where value = 'viid_1400' "
        sql00 = "delete from `ifaas_basicinfo`.`t_third_platform_info` where ip = '192.168.11.78'"
        InsertSQL2(sql0,sql00)
        sql = "delete from  ifaas_basicinfo.t_camera_info where  manufacturer = 'hik';"
        InsertSQL1(sql)
    def test_Aviid1400Type(self):
        print "========预置视图库信息========"
        sql1 = "INSERT INTO `ifaas_basicinfo`.`t_base_platform_type` (`id`, `value`, `remark`, `describle`, `create_time`, `update_time`) VALUES ('100', 'viid_1400', NULL, NULL, '2020-03-17 11:42:20', '2020-03-17 11:47:48');"
        sql2 = "INSERT INTO `ifaas_basicinfo`.`t_third_platform_info` (`id`, `type_id`, `name`, `ip`, `port`, `user_name`, `password`, `other`, `remark`, `create_time`, `update_time`, `server_id`, `engine_id`, `platform_code`, `area_id`, `vendor`) VALUES ('10000', '100', '78视图库平台', '192.168.11.78', '10005', 'wangxin', '123456', NULL, NULL, '2020-03-17 11:42:20', '2020-03-19 14:27:07', NULL, NULL, '44000000000000001234', '1', NULL);"
        # 添加视图库信息，与引擎对接
        InsertSQL2(sql1, sql2)
        # 等待十分钟
        time.sleep(5)
        print "视图库信息接入完成"
        time.sleep(300)
    def test_BGetviidcamera(self):
        #AddCamera()#添加摄像头"192.168.8.232"
        self.assertEqual( 1,SelectCamera("192.168.8.8"))  # 断言
        print "摄像头信息同步完成"

    # #启动采集任务
        time.sleep(5)
    def test_Cstart_viidTask(self):
        StartTask("192.168.8.8")
        time.sleep(180)
        SelectTask("192.168.8.8")
        self.assertEqual(1, SelectTask("192.168.8.8"))  # 断言

    """
    通过kafka查看是否有抓拍图片消息上报
    """

    def test_Dstop_viidTask(self):
        StopTask("192.168.8.8")
        time.sleep(180)
        SelectTask("192.168.8.8")
        self.assertEqual(0, SelectTask("192.168.8.8"))  # 断言

    @classmethod
    def tearDownClass(cls):
        sql0 = "delete from `ifaas_basicinfo`.`t_base_platform_type` where value = 'viid_1400' "
        sql00 = "delete from `ifaas_basicinfo`.`t_third_platform_info` where ip = '192.168.11.78'"
        InsertSQL2(sql0,sql00)
        sql = "delete from  ifaas_basicinfo.t_camera_info where  manufacturer = 'hik';"
        InsertSQL1(sql)
        print "数据库信息清理完毕"
if __name__ == '__main__':
    unittest.main(verbosity=2)