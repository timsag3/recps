# -*- coding: utf-8 -*-

from clients_.base_clients import RemoteClient
from command_workers.ssh_command_builder import SSHCommandBuilder


class SSHClient(RemoteClient):

    def __init__(self, password, path_to_pass, raw_command, user_at_host=None):
        super(SSHClient, self).__init__(password=password, path_to_pass=path_to_pass, raw_command=raw_command)
        self._user_at_host = user_at_host
        self._command_builder = SSHCommandBuilder

    def build_command(self):
        command_builder = self._command_builder(user_at_host=self._user_at_host,
                                                password=self._password,
                                                path_to_pass=self._path_to_pass,
                                                command=self._raw_command)
        full_command = command_builder.build_command()
        return full_command
