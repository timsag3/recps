# -*- coding: utf-8 -*-

from clients_.base_clients import AbstractClient


class PerfClient(AbstractClient):

    def __init__(self, server, client):
        super(PerfClient, self).__init__()
        self._server = server
        self._client = client
        print(self.__dict__, '\n')
        print(self._server.__dict__, '\n')
        print(self._client.__dict__, '\n')

    def request(self):
        pass
