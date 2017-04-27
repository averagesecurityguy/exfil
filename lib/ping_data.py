# -*- coding: utf-8 -*-
import sys
import network
import icmp

def listen(port):
    print('Listening for data via ICMP.')
    l = network.get_listener('ICMP')

    print('Data Received:')
    while 1:
        data, _ = icmp.receive(l)

        sys.stdout.write(data)


def send(server, port, data):
    print('Sending data to {0} via ICMP.'.format(server))
    s = network.get_sender('ICMP', server)

    print('Data Sent:')
    for n in range(0, len(data), icmp.BLOCK_SIZE):
        block = data[n:n + icmp.BLOCK_SIZE]
        icmp.send(s, block)

        sys.stdout.write(block)
