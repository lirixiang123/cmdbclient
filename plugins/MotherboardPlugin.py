#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import BasePlugin


class MotherboardPlugin(BasePlugin.BasePlugin):
    """
    获取主板信息：产商，型号，序列号
    :return: {"sn":"sn", "model":"model", "manufactory":"manufactory"}
    """

    def linux(self):
        try:
            shell_command = "sudo dmidecode -t1"
            output = self.exec_shell_cmd(shell_command)
            # from config.settings import BASEDIR
            # output = open(os.path.join(BASEDIR,'files/board.out'), 'r').read()
            return self.parse(output)
        except Exception as e:
            raise Exception('linux motherboard command is exception')

    def windows(self):
        try:
            sn = self.exec_shell_cmd("wmic baseboard get serialnumber").strip().split('\n')[-1]
            manufactory = self.exec_shell_cmd("wmic baseboard get manufacturer").strip().split('\n')[-1]
            model = self.exec_shell_cmd("wmic baseboard get product").strip().split('\n')[-1].split()[-1]
            result = {
                "sn": sn,
                "model": model,
                "manufactory": manufactory
            }
            return result
        except Exception as e:
            raise Exception('windows motherboard command is exception')

    def parse(self, content):
        result = {}
        key_map = {
            # 产商
            'Manufacturer': 'manufactory',
            # 型号
            'Product Name': 'model',
            # 序列号
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]
        return result
