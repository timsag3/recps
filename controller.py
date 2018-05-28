# -*- coding: utf-8 -*-

import argparse
import const


# class RecpsController(object):
#     """
#     Controller interface that parse arguments from
#     command line input and choose model build strategy.
#     """
#
#     @staticmethod
def recps_arg_parser():
    parser = argparse.ArgumentParser(description='desc')
    parser.add_argument('-t', choices=['scp', 'shp', 'ipe'], dest='type')
    user_args = parser.parse_args()
    print(user_args)
recps_arg_parser()