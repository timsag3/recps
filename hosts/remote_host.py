# -*- coding: utf-8 -*-

from hosts import abstract_host


class RemoteHost(abstract_host.Host):
    def __init__(self, user_at_host, password):
        super(RemoteHost, self).__init__(user_at_host=user_at_host, password=password)

    def get_status(self):
        return True
