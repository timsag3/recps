# -*- coding: utf-8 -*-

from clients_.base_clients import RemoteClient
from command_workers.ssh_command_builder import SSHCommandBuilder
from command_workers.command_executor import CommandExecutor


class SSHClient(RemoteClient):

    def __init__(self, password, path_to_pass, command=None, user_at_host=None):
        super(SSHClient, self).__init__(password=password, path_to_pass=path_to_pass)
        self._user_at_host = user_at_host
        self._command = command
        self._full_command = self.build_command()

    def build_command(self):
        command_builder = SSHCommandBuilder(user_at_host=self._user_at_host,
                                            password=self._password,
                                            path_to_pass=self._path_to_pass,
                                            command=self._command)
        full_command = command_builder.build_command()
        return full_command

    def request(self):
        data = CommandExecutor.exec_command(self._full_command)
        return data
