# -*- coding: utf-8 -*-

from clients.ssh_client import SSHClient


class ScpClient(SSHClient):

    def __init__(self, auth_type, target, destination):
        super(ScpClient, self).__init__(auth_type=auth_type)
        self.auth_type = auth_type
        self.target = target
        self.destination = destination
