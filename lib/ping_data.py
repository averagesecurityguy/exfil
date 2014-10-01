# -*- coding: utf-8 -*-
import network

BLOCK_SIZE = 256

def listen(port):
    print('Listening for data via ICMP.')
    l = network.get_listener('ICMP')

    print('Data Received:')
    while 1:
        data, addr = l.recvfrom(1500)

        # Drop the first 24 bytes because it is header data.
        print network.decode_data(data[24:])


def send(server, port, data):
    print('Sending data to {0} via ICMP.'.format(server))
    s = network.get_sender('ICMP', server)

    print('Data Sent:')
    for n in range(0, len(data), BLOCK_SIZE):
        block = data[n:n + BLOCK_SIZE]
        print(block)

        enc = network.encode_data(block)
        icmp = network.build_icmp_echo(data=enc)

        s.send(str(icmp))