# -*- coding: utf-8 -*-

from clients_.ssh_client import RemoteClient
from command_workers.scp_command_builder import SCPCommandBuilder


class SCPClient(RemoteClient):

    def __init__(self, password, path_to_pass, source, destination):
        super(SCPClient, self).__init__(password=password, path_to_pass=path_to_pass)
        self._source = source
        self._destination = destination
        self._command_builder = SCPCommandBuilder

    def build_command(self):
        command_builder = self._command_builder(source=self._source,
                                                destination=self._destination,
                                                password=self._password,
                                                path_to_pass=self._path_to_pass)
        full_command = command_builder.build_command()
        return full_command
