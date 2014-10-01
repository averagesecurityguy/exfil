# -*- coding: utf-8 -*-
import network

BLOCK_SIZE = 224
PORT = 53

def listen(port):
    if port is None:
        port = PORT

    print('Listening for data via DNS on port {0}.'.format(port))
    l = network.get_listener('UDP', port)

    print('Data Received:')
    while 1:
        data, addr = l.recvfrom(1500)

        dns = network.parse_dns(data)
        name = str(dns.get_q().get_qname()) 
        dec = network.decode_data(name.rstrip('.'))
        print(dec)


def send(server, port, data):
    if port is None:
        port = PORT

    print('Sending data via DNS to {0} on port {1}.'.format(server, port))

    print('Data Sent:')
    for n in range(0, len(data), BLOCK_SIZE):
        block = data[n:n + BLOCK_SIZE]
        print(block)

        enc = network.encode_data(block)
        network.send_dns_query(server, port, enc)
