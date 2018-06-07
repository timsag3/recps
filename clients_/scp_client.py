# -*- coding: utf-8 -*-

from clients_.ssh_client import SSHClient
from command_workers.scp_command_builder import SCPCommandBuilder


class SCPClient(SSHClient):

    def __init__(self, password, path_to_pass, source, destination):
        super(SCPClient, self).__init__(password, path_to_pass)
        self._source = source
        self._destination = destination

    def build_command(self):
        command_builder = SCPCommandBuilder(self._source,
                                            self._destination,
                                            self._password,
                                            self._path_to_pass)
        full_command = command_builder.build_command()
        return full_command

    def request(self):
        pass
