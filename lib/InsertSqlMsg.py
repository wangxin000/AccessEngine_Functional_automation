#! /usr/bin/python
# -*- coding:UTF-8  -*-
import time
import os
import pymysql
from config.config import *

#数据库信息取之于config.py中数据库配置
# 账号密码连接数据库
def InsertSQL2(sql1,sql2):
    conn = pymysql.connect(host = db_host ,port = db_port,user = db_user,passwd = db_passwd,db = db)
# 创建游标
    cursor = conn.cursor()
#插入数据库语句
    cursor.execute(sql1)
    cursor.execute(sql2)
# 提交
    conn.commit()
#关闭
    conn.close()
    cursor.close()
# 等待五分钟
#    time.sleep(600)
def InsertSQL1(sql1):
    conn = pymysql.connect(host = db_host ,port = db_port,user = db_user,passwd = db_passwd,db = db)
# 创建游标
    cursor = conn.cursor()
#插入数据库语句
    cursor.execute(sql1)
#    cursor.execute(sql2)
# 提交
    conn.commit()
#关闭
    conn.close()
    cursor.close()
#返回查询结果
def  ExecuteSQL(sql):
    conn = pymysql.connect(host = db_host ,port = db_port,user = db_user,passwd = db_passwd,db = db)
    # 创建游标
    cursor = conn.cursor()
    # 插入数据库语句
    cursor.execute(sql)
    # 提交
    conn.commit()
    #查询结果
    result = cursor.fetchone()
    # 关闭
    conn.close()
    cursor.close()
    return result[0]
# 添加的摄像头信息
def AddCamera(cameraID,cameraIP,cameraUser,cameraPasswd):
       sql1 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('{0}', '{1}', '8000', '{2}', '{3}', '1', '0', NULL, '', NULL, NULL, '2020-04-16 14:47:04', '2020-04-23 09:48:40', 'POINT(45.000000 56.000000)', NULL, '1', '0', '15F茶水间北侧', '1', '1', NULL, '[{{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"}},{{\"attribute\":[\"coatPattern\",\"coatStyle\",\"gender\",\"angle\",\"bag\",\"ageStage\",\"hasCoat\",\"pantsStyle\",\"pantsPattern\",\"ride\",\"clothColor\"],\"target\":\"body\"}}]', '', '2', '2', NULL, '00:00,24:00', '12', '0', '3bd49fe7-0cc5-400f-baba-15d0d51fe2f9', NULL, NULL, NULL, '', NULL, NULL, '', '', '0', NULL, NULL);".format(cameraID,cameraIP,cameraUser,cameraPasswd)
       #sql1 = "INSERT INTO `ifaas_basicinfo`.`t_camera_info` (`id`, `ip`, `port`, `login_user`, `password`, `area_id`, `capture_type`, `manufacturer`, `camera_code`, `rtsp`, `config`, `created`, `updated`, `geo_string`, `geometry`, `is_enable`, `status`, `name`, `device_type`, `creator`, `creator_name`, `ability`, `channel`, `online`, `snap`, `node_id`, `abnormal_time`, `abnormal_hour`, `nvr_id`, `bank_id`, `collection_type`, `extend_long_field1`, `extend_long_field2`, `move_direction`, `type`, `sync_token`, `label`, `vendor`, `equipment_type`, `source_id`, `url`) VALUES ('10000000', '192.168.8.232', '8000', 'admin', 'introcks1234', '1', '0', NULL, '', NULL, NULL, '2020-04-16 14:47:04', '2020-04-23 09:48:40', 'POINT(45.000000 56.000000)', NULL, '1', '0', '15F茶水间北侧', '1', '1', NULL, '[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"},{\"attribute\":[\"coatPattern\",\"coatStyle\",\"gender\",\"angle\",\"bag\",\"ageStage\",\"hasCoat\",\"pantsStyle\",\"pantsPattern\",\"ride\",\"clothColor\"],\"target\":\"body\"}]', '', '2', '2', NULL, '00:00,24:00', '12', '0', '3bd49fe7-0cc5-400f-baba-15d0d51fe2f9', NULL, NULL, NULL, '', NULL, NULL, '', '', '0', NULL, NULL);"
       InsertSQL1(sql1)
#删除对应id的摄像头
def DeleteCamera(cameraip):
    #cameraip = ip
    sql = "delete from `ifaas_basicinfo`.`t_camera_info` where ip = '{0}'".format(cameraip)
    InsertSQL1(sql)
#启动对应ip的摄像头任务
def StartTask(cameraip):
    #cameraip = ip
    sql = "update ifaas_basicinfo.t_camera_info set `status` = 1 where ip = '{0}'".format(cameraip)
    InsertSQL1(sql)
#停止对应ip的摄像头任务
def StopTask(cameraip):
    #cameraip = ip
    sql = "update ifaas_basicinfo.t_camera_info set `status` = 0 where ip = '{0}'".format(cameraip)
    InsertSQL1(sql)

#查询对应摄像头id的任务是否启动
def SelectTask(cameraip):
    # sourceid = source_id
     sql = "SELECT COUNT(*) from ifaas_center.t_task_info where source_id in (SELECT id from ifaas_basicinfo.t_camera_info where ip = '{0}')".format(cameraip)
     ExecuteSQL(sql)
     return ExecuteSQL(sql)
#查询摄像头信息是否添加成功
def SelectCamera(cameraip):
    #cameraip = ip
    sql = "SELECT COUNT(*) from ifaas_basicinfo.t_camera_info where ip = '{0}'".format(cameraip)
    ExecuteSQL(sql)
    return ExecuteSQL(sql)