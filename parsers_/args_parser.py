# -*- coding: utf-8 -*-

import argparse


class ArgParser(object):

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Python wrapper on ssh/scp and iperf utilities.')
        parser.add_argument('-f',
                            metavar='/path/to/file',
                            help='read the password from the first line of the file',
                            dest='path_to_pass')
        parser.add_argument('-p', metavar='password',
                            help='provide password as argument (security unwise)',
                            dest='password')

        subparsers = parser.add_subparsers(help='sub-command help')

        parser_ssh = subparsers.add_parser('ssh',
                                           help='execute remote command using secure shell')
        parser_ssh.add_argument('user_at_host',
                                metavar='username@hostname')
        parser_ssh.add_argument('cmd',
                                metavar='command')

        parser_scp = subparsers.add_parser('scp',
                                           help='copy file from/to remote host using secure shell '
                                                'Note: you cannot use it for remote-remote copy.')
        parser_scp.add_argument('source',
                                metavar='[u@h:]/path/to/source')
        parser_scp.add_argument('destination',
                                metavar='[u@h:]/path/to/destination')

        parser_iperf = subparsers.add_parser('iperf',
                                             help='perform network using iperf utility.'
                                                  'Note: you cannot use it for remote-remote perform.')
        parser_iperf.add_argument('server',
                                  metavar='server',
                                  help='local or username@hostname')
        parser_iperf.add_argument('client',
                                  metavar='client',
                                  help='username@hostname or local')
        args = parser.parse_args()
        args_dict = args.__dict__
        if len(args_dict) == 2:
            return parser.parse_args(['-h'])
        return args_dict
