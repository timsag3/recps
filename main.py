#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python Wrapper on ssh, sshpass, scp and ipref utilities.
Provides non interactive remote POSIX commands e.i. 'ls',
'df', 'ps' etc, copying files and perform network throughput
tests in remote-local and local-remote modes with the
possibility to enter password as command argument and read
it from the file.
"""

from parsers_.args_parser import ArgParser
from client_buliders.client_builders_manager import ClientManager


def main():
    args = ArgParser.get_args()
    client_manager = ClientManager(args)
    client = client_manager.get_client()
    response = client.request()
    return response


if __name__ == "__main__":
    main()
