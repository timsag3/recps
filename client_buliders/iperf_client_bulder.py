# -*- coding: utf-8 -*-

from client_buliders.base_client_builder import ClientBuilder
from clients_.iperf_client import PerfClient
from clients_.base_clients import Client
from clients_.ssh_client import SSHClient


class PerfClientBuilder(ClientBuilder):
    def __init__(self, data):
        super(PerfClientBuilder, self).__init__(data)
        self._server_cmd = 'iperf -s -t 12'
        self._client_cmd = 'iperf -c {}'

    def build_client(self):
        server = self._data['server']
        client = self._data['client']
        if server == 'local' and client != 'local':
            client_ip = input('Enter your local IP address: ')
            perf_server = Client(self._server_cmd)
            perf_client = SSHClient(password=self._password,
                                    path_to_pass=self._path_to_pass,
                                    user_at_host=client,
                                    raw_command=self._client_cmd.format(client_ip))
        elif server != 'local' and client == 'local':
            server_ip = self._data['server'].split('@')[1]
            perf_server = SSHClient(password=self._password,
                                    path_to_pass=self._path_to_pass,
                                    user_at_host=server,
                                    raw_command=self._server_cmd)
            perf_client = Client(self._client_cmd.format(server_ip))
        else:
            print('Performance two remote hosts not realized yet!')
            return
        return PerfClient(server=perf_server, client=perf_client)
