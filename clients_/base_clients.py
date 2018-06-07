# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from command_workers.command_executor import CommandExecutor


class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def request(self):
        """
        :return: byte sequence
        """


class Client(AbstractClient):

    def __init__(self, command=None):
        super(Client, self).__init__()
        self._command = command

    @abstractmethod
    def request(self):
        raise NotImplementedError


class LocalClient(Client):
    def __init__(self, command):
        super(LocalClient, self).__init__(command=command)

    def request(self):
        response = CommandExecutor.exec_command(self._command)
        return response


class RemoteClient(Client):
    def __init__(self, password, path_to_pass):
        super(RemoteClient, self).__init__()
        self._password = password
        self._path_to_pass = path_to_pass

    @abstractmethod
    def build_command(self):
        raise NotImplementedError
