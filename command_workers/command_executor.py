# -*- coding: utf-8 -*-

import subprocess


class CommandExecutor(object):

    @staticmethod
    def exec_command(command):
        cmd_list = command.split(' ')
        process = subprocess.Popen(cmd_list, shell=False)
        process.communicate()
        return True
