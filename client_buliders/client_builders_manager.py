# -*- coding: utf-8 -*-

from client_buliders.ssh_client_builder import SSHClientBuilder
from client_buliders.scp_client_builder import SCPClientBuilder
from client_buliders.iperf_client_bulder import PerfClientBuilder


class ClientManager(object):

    def __init__(self, user_args):
        self._data = user_args

    def get_client(self):
        client = 'undefined'
        if 'user_at_host' in self._data:
            client = SSHClientBuilder.build_client(self._data)
        elif 'source' and 'destination' in self._data:
            client = SCPClientBuilder.build_client(self._data)
        elif 'server' and 'client' in self._data:
            client = PerfClientBuilder.build_client(self._data)
        return client
