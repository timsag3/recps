# -*- coding: utf-8 -*-


class BaseCommandBuilder(object):

    def __init__(self, password, path_to_pass):
        self._password = password
        self._path_to_pass = path_to_pass
        self._sshpass_pref = self.get_sshpass_pref()
        self._main_prefix = self.get_main_pref()

    def get_sshpass_pref(self):
        password = self._password
        path_to_pass = self._path_to_pass
        if password:
            return f'sshpass -p {password} '
        elif path_to_pass:
            return f'sshpass -f {path_to_pass} '
        else:
            return ''

    def get_main_pref(self):
        raise NotImplementedError

    def build_command(self):
        raise NotImplementedError
