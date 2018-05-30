# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractClient(metaclass=ABCMeta):

    def __init__(self, host=None, command=None):
        self._host = host
        self._command = command

    @abstractmethod
    def send_request(self, command: object) -> list:
        raise NotImplementedError()

    @abstractmethod
    def send_result(self, result):
        raise NotImplementedError()
