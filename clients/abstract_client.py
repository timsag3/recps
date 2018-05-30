# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractClient(metaclass=ABCMeta):

    def __init__(self, host=None, command=None, prefix=None):
        self._server = host
        self._posix_command = command
        self._prefix = prefix

    @abstractmethod
    def get_prefix(self):
        raise NotImplementedError()

    @abstractmethod
    def send_request(self):
        raise NotImplementedError()

    @abstractmethod
    def send_result(self, result):
        raise NotImplementedError()

    @abstractproperty
    def server(self):
        raise NotImplementedError()

    @abstractproperty
    def prefix(self):
        raise NotImplementedError()

    @abstractproperty
    def posix_command(self):
        raise NotImplementedError()
