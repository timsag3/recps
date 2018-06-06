# -*- coding: utf-8 -*-

from clients_.base_client import Client
from command_builders.ssh_command_builders import SSHCommandBuilder


class SSHClient(Client):

    def __init__(self, remote_host, command=None):
        super(SSHClient, self).__init__(command)
        self.remote_host = remote_host
        self._command_builder = SSHCommandBuilder(self)

    def send_request(self):
        full_command = self._command_builder.build_command()
        data = self.executor.exec_command(full_command)
        return data
