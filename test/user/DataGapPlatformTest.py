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
from lib.kafkatTopic import *
#  -------------------数据网关平台数据构造--------------------------


# 第一步插入第三方数据库信息
# 账号密码连接数据库\

class TestDataGapPlatform(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
       sql = "delete from `ifaas_basicinfo`.`t_base_platform_type` where id = 500"
       sql1 = "delete from `ifaas_basicinfo`.`t_third_platform_info`  where id = 10100"
       InsertSQL2(sql,sql1)

    def test_AddDataGap(self):

        sql1 = "INSERT INTO `ifaas_basicinfo`.`t_base_platform_type` (`id`, `value`, `remark`, `describle`, `create_time`, `update_time`) VALUES ('500', 'deep_eye', NULL, NULL, '2020-05-27 11:14:35', '2020-05-27 11:14:39');"
        sql2 = "INSERT INTO `ifaas_basicinfo`.`t_third_platform_info` (`id`, `type_id`, `name`, `ip`, `port`, `user_name`, `password`, `other`, `remark`, `create_time`, `update_time`, `server_id`, `engine_id`, `platform_code`, `area_id`, `vendor`) VALUES ('10100', '500', '42数据网关平台', '192.168.11.42', '3019', 'admin', 'admin1234', NULL, NULL, '2020-05-19 19:47:44', '2020-05-19 19:47:47', NULL, NULL, NULL, '1', NULL);"
        # 添加数据网关平台信息

        InsertSQL2(sql1, sql2)
        # 等待
        time.sleep(300)
        print "数据网关数据插入OK，请查看中心引擎和引擎中心日志查看是否有success日志"

        """
        （1）添加完之后，中心服务器从基础数据服务，
        获取信息：grep '数据网关平台' intellif_engine_info.log
         日志关键字：open platform access successful
        （2）接入引擎通过中心服务器获取视图平台信息
        获取信息：grep '数据网关平台' IFaceEngin.log
        日志关键字：OpenPlatformAccess begin
        """
        # time.sleep(300)
        # 通过同步过来的摄像头名称，断言是否同步摄像头正常
        sql3 = "select count(*) from `ifaas_basicinfo`.`t_camera_info` where port = 0"
        ExecuteSQL(sql3)
        self.assertGreaterEqual(ExecuteSQL(sql3),1)
        """

        添加用例，判断kafka消息输出
        """

    @classmethod
    def tearDownClass(cls):

        print "==========tearDown======"
        sql = "delete from `ifaas_basicinfo`.`t_base_platform_type` where id = 500"
        sql1 = "delete from `ifaas_basicinfo`.`t_third_platform_info`  where id = 10100"
        InsertSQL2(sql, sql1)
        sql232= "delete from `ifaas_basicinfo`.`t_camera_info` where port = 0"
        InsertSQL1(sql232)
        print "信息删除完毕"
if __name__ == '__main__':
    unittest.main(verbosity=2)
