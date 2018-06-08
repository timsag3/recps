# -*- coding: utf-8 -*-

from clients_.base_clients import AbstractClient


class PerfClient(AbstractClient):

    def __init__(self, server, client):
        super(PerfClient, self).__init__()
        self._server = server
        self._client = client

    def request(self):
        server_data = self._server.request()
        client_data = self._client.request()
        return server_data, client_data
