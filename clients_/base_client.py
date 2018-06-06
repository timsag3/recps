# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from command_workers.command_executor import CommandExecutor


class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def request(self):
        raise NotImplementedError


class LocalClient(AbstractClient):

    def __init__(self, command):
        super(LocalClient, self).__init__()
        self._command = command

    def request(self):
        command_executor = CommandExecutor
        command = self._command
        response = command_executor.exec_command(command)
        return response


class RemoteClient(AbstractClient):
    def __init__(self):
        super(RemoteClient, self).__init__()

    @abstractmethod
    def build_command(self):
        raise NotImplementedError
