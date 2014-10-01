# -*- coding: utf-8 -*-
import socket
import dpkt
import dnslib
import base64


def _get_socket(protocol):
    protocol = protocol.upper()
    if protocol not in ['TCP', 'UDP', 'ICMP']:
        print('Error: Protocol must be one of TCP, UDP, or ICMP.')
        return None

    try:
        if protocol == 'ICMP':
            return socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        elif protocol == 'UDP':
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print('Error: Could not create socket. {0}.'.format(str(e)))
        return None


def encode_data(data):
    return base64.b64encode(data)


def decode_data(data):
    return base64.b64decode(data)


def get_listener(protocol, port=0):
    s = _get_socket(protocol)
    if s is not None:
        s.bind(('0.0.0.0', port))
        return s

    return None


def get_sender(protocol, server):
    s = _get_socket(protocol)
    if s is not None:
        s.connect((server, 1))
        return s

    return None


def build_icmp_echo(id=0, seq=0, data=''):
    echo = dpkt.icmp.ICMP.Echo()
    echo.id = id
    echo.seq = seq
    echo.data = data

    icmp = dpkt.icmp.ICMP()
    icmp.type = dpkt.icmp.ICMP_ECHO
    icmp.data = str(data)

    return icmp


def parse_dns(data):
    return dnslib.DNSRecord.parse(data)


def send_dns_query(server, port, name):
    q = dnslib.DNSRecord.question(name)

    try:
        q.send(server, port=port, timeout=1)

    except socket.timeout:
        pass
