# -*- coding: utf-8 -*-

from client_buliders.base_client_builder import ClientBuilder
from clients_.scp_client import SCPClient


class SCPClientBuilder(ClientBuilder):
    def __init__(self, data):
        super(SCPClientBuilder, self).__init__(data)

    def build_client(self):
        source = self._data['source']
        destination = self._data['destination']
        if '@' in source and '@' in destination:
            print('Copy between two remote hosts not realized yet!')
            return
        return SCPClient(password=self._password,
                         path_to_pass=self._path_to_pass,
                         source=source,
                         destination=destination)
