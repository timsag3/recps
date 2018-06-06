# -*- coding: utf-8 -*-

import argparse

description = 'The wrapper on ssh and iperf utilities with an opportunity sshpass and scp.'


class ArgParser(object):

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument('-t', '--utility type',
                            choices=['ssh', 'scp', 'iperf'],
                            default='ssh',
                            help='utility type, default=ssh',
                            dest='utility_type')
        args = parser.parse_args()
        return args.utility_type
