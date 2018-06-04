# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from command_workers.command_executor import CommandExecutor
from parsers.output_parser import OutputParser


class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def send_request(self):
        raise NotImplementedError

    @abstractmethod
    def show_response(self):
        raise NotImplementedError


class Client(AbstractClient):
    """
    Базовый клиент. Является родителем для ssh клиента. Так же
    может создавать самостоятельные сущности для локальных клиентов.
    """

    def __init__(self, command=None):
        super(Client, self).__init__()
        self.command = command
        self.executor = CommandExecutor
        self.output_parser = OutputParser()

    def send_request(self):
        request = self.executor.exec_command(self.command)
        return request

    def show_response(self):  # :(
        pass

