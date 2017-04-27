# -*- coding: utf-8 -*-
import sys
import network
import dns

def listen(port):
    if port is None:
        port = dns.PORT

    print('Listening for data via DNS on port {0}.'.format(port))
    l = network.get_listener('UDP', port)

    print('Data Received:')
    while 1:
        resp = dns.receive(l)
        sys.stdout.write(resp)


def send(server, port, data):
    if port is None:
        port = dns.PORT

    print('Sending data via DNS to {0} on port {1}.'.format(server, port))
    print('Data Sent:')

    for n in range(0, len(data), dns.BLOCK_SIZE):
        block = data[n:n + dns.BLOCK_SIZE]
        dns.send(server, port, block)

        sys.stdout.write(block)
