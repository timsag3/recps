# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractCommandBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_command(self):
        """
        :return: command string
        """


class SSHPassPrefixGetter(object):

    def __init__(self, password, path_to_pass):
        self._password = password
        self._path_to_pass = path_to_pass
        self._sshpass_pref = self.get_sshpass_prefix()

    def get_sshpass_prefix(self):
        password = self._password
        path_to_pass = self._path_to_pass
        if password:
            return f'sshpass -p {password} '
        elif path_to_pass:
            return f'sshpass -f {path_to_pass} '
        else:
            return ''
