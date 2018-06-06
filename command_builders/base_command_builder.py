# -*- coding: utf-8 -*-


class CommandBuilder(object):

    def __init__(self, client):
        self._client = client
        self._command = client.command
        self._sshpass_pref = self.get_sshpass_pref()
        self._pref = self.get_self_pref()

    def get_sshpass_pref(self):
        password = self._client.remote_host.password
        path_to_pass = self._client.remote_host.path_to_pass
        if password:
            return f'sshpass -p {password} '
        elif path_to_pass:
            return f'sshpass -f {path_to_pass} '
        else:
            return None


    def get_self_pref(self):
        raise NotImplementedError

    def build_command(self):
        raise NotImplementedError
