# -*- coding: utf-8 -*-

from command_workers.base_command_builder import BaseCommandBuilder


class SSHCommandBuilder(BaseCommandBuilder):

    def __init__(self, user_at_host, password, path_to_pass, command):
        super(SSHCommandBuilder, self).__init__(password=password,
                                                path_to_pass=path_to_pass)
        self._user_at_host = user_at_host
        self._command = command

    def get_main_pref(self):
        user_at_host = self._user_at_host
        main_prefix = f'ssh {user_at_host} '
        return main_prefix

    def build_command(self):
        ssh_pass_pref = self._sshpass_pref
        main_prefix = self._main_prefix
        command = self._command
        return ssh_pass_pref + main_prefix + command
