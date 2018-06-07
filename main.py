#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python Wrapper on ssh, sshpass, scp and ipref utilities
"""

from parsers_.args_parser import ArgParser
from client_buliders.client_builders_manager import ClientManager


def main():
    args = ArgParser.get_args()
    client_manager = ClientManager(args)
    client = client_manager.get_client()
    request = client.request()
    response = None


if __name__ == "__main__":
    main()
