#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Wrapper on ssh, sshpass, scp and ipref utilities
"""

from parsers_.args_parser import ArgParser
from client_builders.client_manager import ClientManager

if __name__ == "__main__":
    utility_type = ArgParser.get_args()
    client_manager = ClientManager(utility_type)
    client = client_manager.get_client()
    request = client.send_request()
    print(request)
    exit()
