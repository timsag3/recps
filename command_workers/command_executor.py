# -*- coding: utf-8 -*-

import subprocess


class CommandExecutor(object):

    @staticmethod
    def exec_command(command):
        cmd_list = command.split(' ')
        process = subprocess.run(cmd_list, encoding='utf-8',
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        stdout = process.stdout
        stderr = process.stderr
        return_code = process.returncode
        return stdout, stderr, return_code
