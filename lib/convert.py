#!/usr/bin/env python
# -*- coding:utf-8 -*-

def convert_to_int(value,default=0):
    """将一个数据转化为int类型，如果转换失败，则直接返回0"""
    try:
        result = int(value)
    except Exception as e:
        result = default

    return result

def convert_mb_to_gb(value,default=0):
    """"""
    try:
        value = value.strip('MB')
        result = int(value)
    except Exception as e:
        result = default

    return result