# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Host(metaclass=ABCMeta):

    def __init__(self, user_at_host=None, password=None):
        self._user_at_host = user_at_host
        self._password = password

    @abstractmethod
    def get_status(self):
        raise NotImplementedError()
