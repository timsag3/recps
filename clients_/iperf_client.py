# -*- coding: utf-8 -*-

from clients_.base_client import AbstractClient


class PerfClient(AbstractClient):

    def __init__(self, server, client):
        super(PerfClient, self).__init__()
        self._server = server
        self._client = client

    def request(self):
        pass
