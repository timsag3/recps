#!usr/bin/python
# -*- coding: utf-8 -*-

"""
This module is a wrapper over 'ssh', 'sshpass',
'scp' and 'iperf' utilities.
"""

import subprocess

command = ''


def run_command(command):
    p1 = subprocess.run(command, shell=True)
    print(p1)


if __name__ == '__main__':
    run_command(command)
