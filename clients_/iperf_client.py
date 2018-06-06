# -*- coding: utf-8 -*-

from clients_.base_client import AbstractClient


class IperfClient(AbstractClient):

    def __init__(self, user_args):
        super(IperfClient, self).__init__()
        self._server = None
        self._client = None

    def request(self):
        pass
