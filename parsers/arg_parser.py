# -*- coding: utf-8 -*-

import argparse


class ArgParser(object):

    @staticmethod
    def results():
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--type',
                            choices=['ssh', 'scp', 'iperf'],
                            default='ssh',
                            help='utility type, default = ssh',
                            dest='utility_type')
        parser.add_argument('-a', '--authentication',
                            choices=['pass', 'file'],
                            default=None,
                            help='authentication type, default=None',
                            dest='auth_aype')
        args = parser.parse_args()
        return args
