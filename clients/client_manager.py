# -*- coding: utf-8 -*-

from clients import iperf_client, ssh_client, scp_client
from parsers.arg_parser import ArgParser


class ClientManager(object):
    """
    Ядро модуля. Определяет сущности каких клиетнов должны быть
    созданы для выполнения запроса пользователя.
    """
    def __init__(self):
        self.args = ArgParser.results()
        self.utility_type = self.args.utility_type
        self.auth_type = self.args.auth_type
        self.client_type = self.get_client()

    def get_client(self):
        if self.utility_type == 'ssh':
            return ssh_client.SSHClient(auth_type=self.auth_type)
        elif self.utility_type == 'scp':
            return scp_client.ScpClient(auth_type=self.auth_type, target=None, destination=None)
        elif self.utility_type == 'iperf':
            return iperf_client.IperfClient(client_host=None, server_host=None)
