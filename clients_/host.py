# -*- coding: utf-8 -*-


class Host(object):

    def __init__(self, user_at_host):
        self.user_at_host = user_at_host
        self.password = self.get_password() if self.user_at_host != 'local' else None
        self.path_to_pass = self.get_pass_to_pass() if self.user_at_host != 'local' else None

    def get_password(self):
        password = input(f'Enter a password for {self.user_at_host}(press return to skip): ')
        return password

    def get_pass_to_pass(self):
        if self.password:
            return None
        pass_to_pass = input(f'Enter /path/to/pass_file for {self.user_at_host}(press return to skip): ')
        return pass_to_pass
