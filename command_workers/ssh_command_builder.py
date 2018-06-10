# -*- coding: utf-8 -*-

from command_workers.base_command_builder import AbstractCommandBuilder, SSHPassPrefixGetter


class SSHCommandBuilder(AbstractCommandBuilder, SSHPassPrefixGetter):

    def __init__(self, user_at_host, password, path_to_pass, raw_command):
        super(SSHCommandBuilder, self).__init__(password=password,
                                                path_to_pass=path_to_pass)
        self._user_at_host = user_at_host
        self._command = raw_command
        self._main_prefix = self.get_main_prefix()

    def get_main_prefix(self):
        user_at_host = self._user_at_host
        main_prefix = f'ssh {user_at_host} '
        return main_prefix

    def build_command(self):
        ssh_pass_prefix = self._sshpass_prefix
        main_prefix = self._main_prefix
        command = self._command
        return ssh_pass_prefix + main_prefix + command
