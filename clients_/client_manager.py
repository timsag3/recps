# -*- coding: utf-8 -*-

from clients_.ssh_client import SSHClient
from clients_.scp_client import SCPClient
from clients_.iperf_client import IperfClient


class ClientManager(object):

    def __init__(self, args):
        self.args = args

    def get_client(self):
        client = 'undefined'
        user_args = self.args
        if 'user_at_host' in user_args:
            client = SSHClient(user_args)
        elif 'source' and 'destination' in user_args:
            client = SCPClient(user_args)
        elif 'server' and 'client' in user_args:
            client = IperfClient(user_args)
        return client
