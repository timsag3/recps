# -*- coding: utf-8 -*-

from clients_.ssh_client import SSHClient
from command_workers.scp_command_builder import SCPCommandBuilder


class SCPClient(SSHClient):

    def __init__(self, user_args):
        super(SCPClient, self).__init__(user_args)
        self._source = user_args['source']
        self._destination = user_args['destination']

    def build_command(self):
        command_builder = SCPCommandBuilder(self._source,
                                            self._destination,
                                            self._password,
                                            self._path_to_pass)
        full_command = command_builder.build_command()
        return full_command

    def request(self):
        pass
