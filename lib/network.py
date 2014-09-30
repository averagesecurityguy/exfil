# -*- coding: utf-8 -*-
import socket
import dpkt
import random

def icmp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.bind(('0.0.0.0', 0))

    return s


def icmp_client(server):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.connect((server, 1))

    return s


def build_echo(data):
    echo = dpkt.icmp.ICMP.Echo()
    echo.id = random.randint(0, 0xffff)
    echo.seq = random.randint(0, 0xffff)
    echo.data = data

    icmp = dpkt.icmp.ICMP()
    icmp.type = dpkt.icmp.ICMP_ECHO
    icmp.data = str(echo)

    return icmp