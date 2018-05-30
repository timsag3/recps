# -*- coding: utf-8 -*-

from clients import ssh_client


class PrefixBuilder(object):
    ssh_prefix = 'ssh'

    @staticmethod
    def build_prefix(client):
        if isinstance(client, ssh_client.SSHClient):
            prefix = PrefixBuilder.ssh_prefix + client.server
