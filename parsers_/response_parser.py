# -*- coding: utf-8 -*-

import json


class ResponseParser(object):

    @staticmethod
    def parse_data(raw_data):
        output_str = ''
        stdout, stderr, return_code = raw_data
        output_str += stdout + stderr
        if 'Server listening' in stdout:
            return output_str
        if return_code != 0:
            output_str += 'Failed!\nexit code: ' + str(return_code)
        print(output_str)
        return output_str
