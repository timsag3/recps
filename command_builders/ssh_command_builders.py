# -*- coding: utf-8 -*-

from command_builders.base_command_builder import CommandBuilder


class SSHCommandBuilder(CommandBuilder):

    def __init__(self, client):
        super(SSHCommandBuilder, self).__init__(client)

    def get_self_pref(self):
        user_at_host = self._client.remote_host.user_at_host
        return f'ssh {user_at_host} '

    def build_command(self):
        if not self._sshpass_pref:
            return self._pref + self._command
        else:
            return self._sshpass_pref + self._pref + self._command
