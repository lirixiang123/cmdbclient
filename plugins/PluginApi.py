#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .CpuPlugin import CpuPlugin
from .MemoryPlugin import MemoryPlugin
from .MotherboardPlugin import MotherboardPlugin
from .NicPlugin import NicPlugin
from .DiskPlugin import DiskPlugin
from lib.response import BaseResponse
from lib import log



def get_server_info():
    """获取服务器各种信息"""
    response = BaseResponse()
    try:
        server_info = {}
        disk = DiskPlugin()
        mem = MemoryPlugin()
        board = MotherboardPlugin()
        nic = NicPlugin()
        cpu = CpuPlugin()

        hostname = board.os_hostname()
        sn = board.sn()

        server_info['os_platform'] = board.os_platform()
        server_info['os_version'] = board.os_version()

        # 获取主板信息
        board_info = board.execute()
        server_info.update(board_info)

        # 获取CPU信息
        cpu_info = cpu.execute()
        server_info.update(cpu_info)

        # 获取磁盘信息
        server_info['disk'] = disk.execute()
        if not server_info['disk'].get('status'):
            log.write_error_log('[%s][disk],%s' % (hostname, server_info['disk'].get('error',"数据获取失败")))
            if server_info['disk'].get('error'):
                del server_info['disk']['error']

        # 获取内存信息
        server_info['memory'] = mem.execute()
        if not server_info['memory'].get('status'):
            log.write_error_log('[%s][memory],%s' % (hostname, server_info['memory'].get('error',"内存数据获取失败")))
            if server_info['memory'].get('error'):
                del server_info['memory']['error']

        # 获取网卡信息
        server_info['nic'] = nic.execute()
        if not server_info['nic'].get('status'):
            log.write_error_log('[%s][nic],%s' % (hostname, server_info['nic'].get('error',"网卡数据获取失败")))
            if server_info['nic'].get('error'):
                del server_info['nic']['error']

        response.data = server_info
        response.status = True
    except Exception as e:
        response.message = str(e)
    return response


if __name__ == '__main__':
    ret = get_server_info()
    print(ret.__dict__)
    for k,v in ret.data.items():
        print(k,v)