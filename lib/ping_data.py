# -*- coding: utf-8 -*-
import socket
import network

BLOCK = 128

def listen(port):
    print('Listening for data via ICMP.')
    
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.ntohs(0x0003))
    s.bind(('0.0.0.0', 0))

    print('Data Received:')
    while 1:
        data, addr = s.recvfrom(1508)
        print(data)


def send(server, port, data):
    print('Sending data to {0} via ICMP.'.format(server))

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.connect((server, 1))

    print('Data Sent:')
    for n in range(0, len(data), BLOCK):
        chunk = data[n:n+BLOCK]
        icmp = network.build_echo(chunk)

        print repr(icmp)
        s.send(str(icmp))