# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from command_workers.command_executor import CommandExecutor
from parsers.response_parser import ResponseParser


class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def request(self):
        pass


class Client(AbstractClient):
    def __init__(self, raw_command=None):
        super().__init__()
        self._raw_command = raw_command
        self._command_executor = CommandExecutor
        self._response_parser = ResponseParser

    def request(self):
        raw_data = self._command_executor.exec_command(self._raw_command)
        parsed_data = self._response_parser.parse_data(raw_data)
        return parsed_data


class RemoteClient(Client):
    def __init__(self, password, path_to_pass, raw_command=None, user_at_host=None):
        super().__init__(raw_command=raw_command)
        self._user_at_host = user_at_host
        self._password = password
        self._path_to_pass = path_to_pass
        self._full_command = None

    def request(self):
        raw_data = self._command_executor.exec_command(self._full_command)
        parsed_data = self._response_parser.parse_data(raw_data)
        return parsed_data
