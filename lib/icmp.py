# -*- coding: utf-8 -*-
import dpkt
import network

BLOCK_SIZE = 256

def _build_icmp_echo(id=0, seq=0, data=''):
    echo = dpkt.icmp.ICMP.Echo()
    echo.id = id
    echo.seq = seq
    echo.data = data

    icmp = dpkt.icmp.ICMP()
    icmp.type = dpkt.icmp.ICMP_ECHO
    icmp.data = str(data)

    return icmp


def send(s, data):
    enc = network.encode_data(data)
    icmp = _build_icmp_echo(data=enc)
    count = s.send(bytes(icmp))

    return count


def receive(s):
    resp, addr = s.recvfrom(1500)
    data = network.decode_data(resp[24:].strip())  # Drop 24 bytes of header data.

    return data, addr
