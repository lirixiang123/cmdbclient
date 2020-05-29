#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
import json

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from plugins import PluginApi

# 获取所有数据 (v是一个BaseResponse类)
v = PluginApi.get_server_info()
print(json.dumps(v.__dict__))
# 将数据写入接口
# create_nic(v.__dict__['data']['nic'])

# for k,v in v.__dict__['data'].items():
#     print(k,v)

# insert nic data
# print(v.__dict__['data']['nic'])
# create_nic(v.__dict__['data']['nic'])






