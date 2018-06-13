# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractCommandBuilder(metaclass=ABCMeta):

    @abstractmethod
    def _build_command(self):
        """
        :return: command string
        """


class SSHPassPrefixGetter:

    def __init__(self, password=None, path_to_pass=False):
        self._password = password
        self._path_to_pass = path_to_pass

    def _get_ssh_pass_prefix(self):
        if self._password is not None:
            return f'sshpass {"-f" if self._path_to_pass else "-p"} {self._password}'
        return ''
