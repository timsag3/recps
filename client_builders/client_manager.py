# -*- coding: utf-8 -*-

from client_builders.ssh_scp_client_builder import SSHScpClientBuilder
from client_builders.iperf_client_builder import IperfClientBuilder


class ClientManager(object):

    def __init__(self, utility_type):
        self._utility_type = utility_type

    def get_client(self):
        client = 'undefined'
        if self._utility_type == 'iperf':
            client = IperfClientBuilder.build_client()
        elif self._utility_type == 'ssh' or 'scp':
            client = SSHScpClientBuilder.build_client(self._utility_type)
        return client
