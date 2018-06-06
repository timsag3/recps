# -*- coding: utf-8 -*-

from command_builders.base_command_builder import CommandBuilder


class ScpCommandBuilder(CommandBuilder):

    def __init__(self, client):
        super(ScpCommandBuilder, self).__init__(client)

    def get_self_pref(self):
        mode = self._client.mode
        user_at_host = self._client.remote_host.user_at_host
        target = self._client.target
        destination = self._client.destination
        pref = None
        if mode == '1':
            pref = f'scp {target} {user_at_host}:{destination}'
        elif mode == '2':
            pref = f'scp {user_at_host}:{target} {destination}'
        return pref

    def build_command(self):
        if not self._sshpass_pref:
            return self._pref
        else:
            return self._sshpass_pref + self._pref
