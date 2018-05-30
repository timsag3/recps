# -*- coding: utf-8 -*-

from hosts import abstract_host


class LocalHost(abstract_host.Host):
    def __init__(self, password):
        super(LocalHost, self).__init__(password=password)

    def get_status(self):
        return True
