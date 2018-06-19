# -*- coding: utf-8 -*-

from command_workers.base_command_builder import AbstractCommandBuilder, SSHPassPrefixGetter


class SCPCommandBuilder(AbstractCommandBuilder, SSHPassPrefixGetter):

    def __init__(self, source, destination, password, path_to_pass):
        super().__init__(password=password, path_to_pass=path_to_pass)
        self._source = source
        self._destination = destination
        self._main_prefix = self._get_main_pref()

    def _get_main_pref(self):
        source = self._source
        destination = self._destination
        main_prefix = f'scp -rp {source} {destination}'
        return main_prefix

    def build_command(self):
        ssh_pass_prefix = self._get_ssh_pass_prefix
        main_prefix = self._main_prefix
        return f'{ssh_pass_prefix} {main_prefix}'
