# -*- coding: utf-8 -*-

from client_buliders.base_client_builder import ClientBuilder
from clients_.ssh_client import SSHClient


class SSHClientBuilder(ClientBuilder):
    def __init__(self, data):
        super(SSHClientBuilder, self).__init__(data)

    def build_client(self):
        user_at_host = self._data['user_at_host']
        command = self._data['cmd']
        return SSHClient(password=self._password,
                         path_to_pass=self._path_to_pass,
                         user_at_host=user_at_host,
                         command=command)
