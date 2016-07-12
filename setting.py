#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'



'''
    配置系统相关的参数,提供全局的相关配置
'''
import os
import sys

#获取当前文件路径
root_dir = '\\'.join(os.path.realpath(__file__).split('\\')[:-1])

#url地址
url = 'http://120.197.58.120:9090/Sourcepool'
#print(url + '/httpservice/index.html?method=setYuyue')

sys.path.append(root_dir)
# log等级,1:notset 2:debug  3:info 4:warning 5:error 6:critical
logLevel = 2
# 日志文件路径
logFile = os.path.join(root_dir, 'logs')
# xml测试结果路径
xmlPath = os.path.join(root_dir,'xmlResult')
print(xmlPath)

# 数据库配置，支持MYSQL、MSSQL、ORACLE
DATABASE = {
    "ENGINE": "MYSQL",
    "HOST": "",
    "PORT": 3306,
    "USER": "",
    "PWD": "",
    "DATABASE": ""
}