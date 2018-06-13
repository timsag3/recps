# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class ClientBuilder(metaclass=ABCMeta):
    def __init__(self, data):
        self._data = data
        self._password = self._data['password']
        self._path_to_pass = self._data['path_to_pass']

    @abstractmethod
    def build_client(self):
        """
        :return: client object
        """
