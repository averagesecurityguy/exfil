# -*- coding: utf-8 -*-
import network

# The DNS query has to be in the format sub.domain.tld and each part can be a
# max of 63 characters. Since we are Base64 encoding the data the actual number
# of bytes we can send in each part is 45. We can send a max of 4 parts, which
# is a total of 180 characters.
BLOCK_SIZE = 180
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
        name = name.replace('.', '')
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
        enc = enc[:63] + '.' + enc[63:126] + '.' + enc[126:189] + '.' + enc[189:]
        network.send_dns_query(server, port, enc)
