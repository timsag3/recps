# -*- coding: utf-8 -*-

from clients import abstract_client
from utils import command_executor, prefix_builder
from parsers import output_parser


class SSHClient(abstract_client.AbstractClient):

    def __init__(self, host, command):
        super(SSHClient, self).__init__(host=host, command=command)
        self._prefix = self.get_prefix()

    def get_prefix(self):
        prefix = prefix_builder.PrefixBuilder.build_prefix(self)
        return prefix

    def send_request(self):
        command_request = self.prefix + self._posix_command
        response = command_executor.CommandExecutor.run_command(command_request)
        return response

    def print_result(self, result):
        parsed_result = output_parser.OutputParser.parse_data(result)
        print(parsed_result)

    @property
    def server(self):
        return self._server

    @property
    def prefix(self):
        return self._prefix

    @property
    def posix_command(self):
        return self._prefix