# -*- coding: utf-8 -*-

from clients_.host import Host
from clients_.scp_client import ScpClient
from clients_.ssh_client import SSHClient


class SSHScpClientBuilder(object):

    @staticmethod
    def build_client(utility_type):
        user_at_host = input('Enter remote username@hostname: ')
        remote_host = Host(user_at_host)
        if utility_type == 'ssh':
            command = input(f'Enter remote command for {user_at_host}: ')
            return SSHClient(remote_host, command)

        elif utility_type == 'scp':
            mode = input('Enter scp mode (1.local-remote, 2.remote-local): ')
            target = input('Enter /path/to/target: ')
            destination = input('Enter /path/to/destination/: ')
            return ScpClient(mode=mode, remote_host=remote_host, target=target, destination=destination)
