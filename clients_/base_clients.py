# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from command_workers.command_executor import CommandExecutor
from parsers_.response_parser import ResponseParser


class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def request(self):
        """
        :return: list sequence [stdout, stderr, return code]
        """


class Client(AbstractClient):
    def __init__(self, raw_command=None):
        super(Client, self).__init__()
        self._raw_command = raw_command
        self._command_executor = CommandExecutor
        self._response_parser = ResponseParser

    def request(self):
        raw_data = self._command_executor.exec_command(self._raw_command)
        parsed_data = self._response_parser.parse_data(raw_data)
        return parsed_data


class RemoteClient(Client):
    def __init__(self, password, path_to_pass, raw_command=None):
        super(RemoteClient, self).__init__(raw_command=raw_command)
        self._password = password
        self._path_to_pass = path_to_pass
        self._command_builder = None
        self._full_command = self.build_command()

    @abstractmethod
    def build_command(self):
        """
        :return: string sequence
        """
