# -*- coding: utf-8 -*-

from clients.base_client import Client
from command_workers.ssh_command_builder import SSHCommandBuilder


class SSHClient(Client):
    """
    Клиент от когорого наследуется scp клиент. Выполняет удалённые комманды
    по ssh протоколу, с возможностью расширениея улилиты sshpass.
    """

    def __init__(self, command=None, user=None, host=None, auth_type=None, password=None, path_to_pass=None):
        super(SSHClient, self).__init__(command)
        self.user = user
        self.host = host
        self.user_at_host = f'{self.user}@{self.host}'
        self.auth_type = auth_type
        self.password = password
        self.path_to_path = path_to_pass
        self.command_builder = SSHCommandBuilder(self)
