# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from command_builders.command_executor import CommandExecutor


class AbstractClient(metaclass=ABCMeta):

    def __init__(self, command=None):
        self.executor = CommandExecutor
        self.command = command

    @abstractmethod
    def send_request(self):
        raise NotImplementedError


class Client(AbstractClient):

    def __init__(self, command=None):
        super(Client, self).__init__(command)

    def send_request(self):
        data = self.executor.exec_command(self.command)
        return data
