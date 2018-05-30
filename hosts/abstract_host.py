# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractHost(metaclass=ABCMeta):

    def __init__(self):
        self._username = None
        self._hostname = None
        self._password = None
        self._status = None

    @abstractmethod
    def get_status(self: object) -> bool:
        raise NotImplementedError()
