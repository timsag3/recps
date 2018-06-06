# -*- coding: utf-8 -*-

from clients_.ssh_client import SSHClient
from command_builders.scp_command_builder import ScpCommandBuilder


class ScpClient(SSHClient):

    def __init__(self, mode, remote_host, target, destination):
        super(ScpClient, self).__init__(remote_host)
        self.mode = mode
        self.target = target
        self.destination = destination
        self._command_builder = ScpCommandBuilder(self)
