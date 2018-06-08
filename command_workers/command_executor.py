# -*- coding: utf-8 -*-

import subprocess


class CommandExecutor(object):

    @staticmethod
    def exec_command(command):
        cmd_list = command.split(' ')
        process = subprocess.run(cmd_list, encoding='utf-8', )
        x = process.stdout
        y = process.stderr
        return x, y
