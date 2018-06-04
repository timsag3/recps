# -*- coding: utf-8 -*-

from clients import ssh_client, scp_client


class SSHCommandBuilder(object):
    """
    Класс является общим билдером комманд для ssh и scp клиентов.
    """
    def __init__(self, client):
        self.client = client
        self.ssh_pref = self.get_ssh_pref()
        self.sshpass_pref = '' if self.client.auth_type is None else self.get_sshpass_pref()

    def get_ssh_pref(self):
        if isinstance(self.client, ssh_client.SSHClient):
            return f'ssh {self.client.user_at_host}'
        elif isinstance(self.client, scp_client.ScpClient):
            return f'scp {self.client.target} {self.client.destination}'

    def get_sshpass_pref(self):
        if self.client.password:
            return f'sshpass -p {self.client.password}'
        elif self.client.path_to_pass:
            return f'sshpass -f {self.client.path_to_pass}'

    def build_command(self):
        return self.sshpass_pref, self.ssh_pref, self.client.command
