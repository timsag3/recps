# -*- coding: utf-8 -*-

from clients_.base_client import RemoteClient
from command_workers.ssh_command_builders import SSHCommandBuilder


class SSHClient(RemoteClient):

    def __init__(self, password, path_to_pass, command=None, user_at_host=None):
        super(SSHClient, self).__init__()
        self._user_at_host = user_at_host
        self._password = password
        self._path_to_pass = path_to_pass
        self._command = command
        self._full_command = self.build_command()

    def build_command(self):
        command_builder = SSHCommandBuilder(self._user_at_host,
                                            self._password,
                                            self._path_to_pass,
                                            self._command)
        full_command = command_builder.build_command()
        return full_command

    def request(self):
        pass
