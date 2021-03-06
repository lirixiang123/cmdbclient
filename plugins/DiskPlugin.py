#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import os

from . import BasePlugin


class DiskPlugin(BasePlugin.BasePlugin):
    def linux(self):
        result = {'status': 0, 'data': {}}

        try:
            # MegaCli是用于获取硬件信息的命令
            # shell_command = "MegaCli  -PDList -aALL"
            # output = self.exec_shell_cmd(shell_command)
            # result['data'] = output
            from config.settings import BASEDIR
            output = open(os.path.join(BASEDIR, 'files/disk.out'), 'r').read()
            result['data'] = self.parse(output)
            result['status'] = 1
        except Exception as e:
            result['error'] = e
        return result

    def windows(self):
        return {}

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:

                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False
