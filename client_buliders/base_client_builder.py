# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractClientBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_client(self):
        """
        :return: client object
        """


class ClientBuilder(AbstractClientBuilder):
    def __init__(self, data):
        super(ClientBuilder, self).__init__()
        self._data = data
        self._password = self._data['password']
        self._path_to_pass = self._data['path_to_pass']

    def build_client(self):
        raise NotImplementedError
