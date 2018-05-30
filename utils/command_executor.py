# -*- coding: utf-8 -*-

import subprocess


class CommandExecutor(object):

    @staticmethod
    def run_command(command):
        response = subprocess.run(command, shell=True)
        return response
