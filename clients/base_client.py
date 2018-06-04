#!/usr/bin/python

from command_workers import command_executor
from abc import ABCMeta, abstractmethod


class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def send_request(self):
        raise NotImplementedError

    @abstractmethod
    def show_response(self):
        raise NotImplementedError


class Client(AbstractClient):
    """
    Базовый клиент от котогого наследуются ssh клиент. Так же
    может создавать самостоятельные сущности для локальных клиентов.
    """
    def __init__(self, command=None):
        super(Client, self).__init__()
        self.command = command
        self.executor = command_executor.CommandExecutor

    def send_request(self):
        request = self.executor.exec_command(self.command)
        return request

    def show_response(self):  # :(
        pass
