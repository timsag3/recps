# -*- coding: utf-8 -*-

from client_buliders.ssh_client_builder import SSHClientBuilder
from client_buliders.scp_client_builder import SCPClientBuilder
from client_buliders.iperf_client_bulder import PerfClientBuilder


class ClientManager(object):

    def __init__(self, user_args):
        self._data = user_args

    def get_client(self):
        client_builder = 'undefined'
        if 'user_at_host' in self._data:
            client_builder = SSHClientBuilder(self._data)
        elif 'source' and 'destination' in self._data:
            client_builder = SCPClientBuilder(self._data)
        elif 'server' and 'client' in self._data:
            client_builder = PerfClientBuilder(self._data)
        client = client_builder.build_client()
        return client
