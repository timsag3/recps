# -*- coding: utf-8 -*-

from clients_.base_client import Client


class IperfClient(Client):

    def __init__(self, server, client):
        super(IperfClient, self).__init__()
        self._server = server
        self._client = client

    def send_request(self):
        server_data = self._server.send_request()
        client_data = self._client.send_request()
        return server_data, client_data
