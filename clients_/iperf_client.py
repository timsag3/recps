# -*- coding: utf-8 -*-

from clients_.base_clients import AbstractClient
from threading import Thread
import time


class PerfClient(AbstractClient):

    def __init__(self, server, client):
        super(PerfClient, self).__init__()
        self._server = server
        self._client = client

    def request(self):
        server_thread = Thread(target=self._server.request)
        client_thread = Thread(target=self._client.request)
        server_thread.start()
        time.sleep(5)
        client_thread.start()
        server_thread.join(), client_thread.join()
