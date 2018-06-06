# -*- coding: utf-8 -*-

from clients_.host import Host
from clients_.iperf_client import IperfClient
from clients_.ssh_client import SSHClient
from clients_.base_client import Client


class IperfClientBuilder(object):
    start_server_cmd = 'iperf -s -t 12'
    start_client_cmd = 'iperf -c {}'

    @staticmethod
    def build_client():

        server_user_at_host = input('Enter iperf SERVER username@hostname or "local" to start it local: ')
        iperf_server_host = Host(server_user_at_host)
        if iperf_server_host.user_at_host == 'local':
            server_client = Client(command=IperfClientBuilder.start_server_cmd)
            local_ip = input('Enter your local network ip: ')
            IperfClientBuilder.start_client_cmd = IperfClientBuilder.start_client_cmd.format(local_ip)
        else:
            server_client = SSHClient(remote_host=iperf_server_host, command=IperfClientBuilder.start_server_cmd)

        client_user_at_host = input('Enter iperf CLIENT username@hostname or "local" to start it local: ')
        if client_user_at_host == 'local':
            host_client = Client(command=IperfClientBuilder.start_client_cmd)
        else:
            host_client = SSHClient(remote_host=iperf_server_host, command=IperfClientBuilder.start_client_cmd)
        return IperfClient(server=server_client, client=host_client)
