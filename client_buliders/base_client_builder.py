# -*- coding: utf-8 -*-


class ClientBuilder(object):
    def __init__(self, data):
        self._data = data
        self._password = self._data['password']
        self._path_to_pass = self._data['path_to_pass']

    def build_client(self):
        raise NotImplementedError
