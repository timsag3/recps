# -*- coding: utf-8 -*-

from clients_.base_client import RemoteClient
from command_workers.ssh_command_builders import SSHCommandBuilder


class SSHClient(RemoteClient):

    def __init__(self, user_args):
        super(SSHClient, self).__init__()
        self._user_at_host = user_args['user_at_host']
        self._password = user_args['password']
        self._path_to_pass = user_args['path_to_pass']
        self._command = user_args['cmd'] if 'cmd' in user_args else None
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
