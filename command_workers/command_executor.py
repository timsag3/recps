# -*- coding: utf-8 -*-

import subprocess


class CommandExecutor(object):
    """
    Общий для всех исполнитель комманд. Простой(?), понятный(?), красивый(?).
    """

    @staticmethod
    def exec_command(command):  # :(
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        data = process.communicate()
        print(data)
