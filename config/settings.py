#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
将结果写入web接口
"""

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.join(BASEDIR)
ERROR_LOG_FILE = os.path.join(BASEDIR, "log", 'error.log')
RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'message.log')
# MQ_SERVER = "192.168.0.1"
# MQ_PORT = "1111"
API = "http://127.0.0.1:8000/cmdbapi"
APPID = 'Appid00002'
SECRETKEY = 'ThisIsSecuretKey0002'
VERSION = "v1"
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
