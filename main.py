#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python Wrapper on ssh, sshpass, scp and ipref utilities
"""

from parsers_.args_parser import ArgParser
from clients_.client_manager import ClientManager

if __name__ == "__main__":
    args = ArgParser.get_args()
    client_manager = ClientManager(args)
    client = client_manager.get_client()
    # request = client.send_request()
    # print(request)
