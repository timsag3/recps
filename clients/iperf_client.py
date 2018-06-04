# -*- coding: utf-8 -*-

from clients.base_client import AbstractClient
from command_workers.iperf_command_builder import IperfCommandBuilder
from parsers.iperf_output_parser import IperfOutputParser


class IperfClient(AbstractClient):
    """
    Наследуется от абстракного клиента и имеет только стандартные
    переопределённые методы. Однако его атрибуты (хосты) являются
    сущностями других клиентов и содержат в себе все необходимые методы
    для выполнения комманд.
    """

    def __init__(self, client_host, server_host):
        super(IperfClient, self).__init__()
        self.server_host = server_host
        self.client_host = client_host
        self.command_builder = IperfCommandBuilder()
        self.output_parser = IperfOutputParser()

    def send_request(self):  # :(
        pass

    def show_response(self):  # :(
        pass
