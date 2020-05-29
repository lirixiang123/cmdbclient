#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import abc
import platform


class BasePlugin(metaclass=abc.ABCMeta):
    def os_platform(self):
        """
        获取操作系统类型：Windows 还是 Linux
        """
        output = platform.system()
        return output.strip()

    def os_version_win(self):
        """
        uname_result(system='Windows', node='PC-201709170950', release='10', version='10.0.14393', machine='AMD64', processor='Intel64 Family 6 Model 78 Stepping 3, GenuineIntel')
        返回版本信息
        """
        return f"{platform.uname().system} {platform.uname().release}"

    # 类中，没有使用实例信息的方法可以直接定义成静态方便，以便不需要实例化直接使用该方法。根据情况决定是否定义成静态方法
    @staticmethod
    def os_version_linux():
        # 自带的方法将被废弃，所以用三方模块来获取
        # return " ".join(platform.linux_distribution())
        import distro
        return " ".join(distro.linux_distribution())

    def os_version(self):
        try:
            if self.os_platform() == "Linux":
                output = self.os_version_linux()
            else:
                output = self.os_version_win()
            result = output.strip()
        except Exception as e:
            result = "got os version failed"
        return result

    def os_hostname(self):
        output = self.exec_shell_cmd('hostname')
        return output.strip()

    def sn_win(self):
        return self.exec_shell_cmd('wmic bios get serialnumber').strip().split()[-1]

    def sn_linux(self):
        return self.exec_shell_cmd("dmidecode | grep 'Serial Number:' | grep -v Not | head -n 1 | awk  '{ print $3 }'")

    def sn(self):
        try:
            if self.os_platform() == "Linux":
                output = self.sn_linux()
            else:
                output = self.sn_win()
            result = output.strip()
        except Exception as ex:
            result = "got sn failed."
        return result

    def exec_shell_cmd(self, cmd):
        import subprocess
        status, output = subprocess.getstatusoutput(cmd)
        return output

    def execute(self):
        if self.os_platform() == "Linux":
            return self.linux()
        else:
            return self.windows()

    @abc.abstractmethod
    def linux(self):
        raise Exception('You must implement Linux method.')

    @abc.abstractmethod
    def windows(self):
        raise Exception('You must implement windows method.')
