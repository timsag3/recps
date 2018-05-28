# -*- coding: utf-8 -*-

import argparse
import const


class RecpsController(object):
    """
    Controller interface that parse arguments from
    command line input and choose model build strategy.
    """

    @staticmethod
    def recps_arg_parser():
        parser = argparse.ArgumentParser(description='desc')
        parser.add_argument('-t', required=True, choices=const.Const.type_choices, dest=const.Const.type_destination)
        parser.add_argument('-p', default=None, dest='password')
        parser.add_argument('-f', default=None, dest='path/to/password')
        parser.add_argument('-h', required=True, dest='host')
        user_args = parser.parse_args()
        print(user_args)
