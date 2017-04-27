# -*- coding: utf-8 -*-
import dnslib
import socket
import network


# The DNS query has to be in the format sub.domain.tld and each part can be a
# max of 63 characters. Since we are Base64 encoding the data the actual number
# of bytes we can send in each part is 45. We can send a max of 4 parts, which
# is a total of 180 characters.
BLOCK_SIZE = 180
PORT = 53

def _parse_dns(data):
    return dnslib.DNSRecord.parse(data)


def _send_dns_query(server, port, name):
    q = dnslib.DNSRecord.question(name)

    try:
        q.send(server, port=port, timeout=1)

    except socket.timeout:
        pass


def send(server, port, data):
    enc = network.encode_data(data)
    enc = enc[:63] + '.' + enc[63:126] + '.' + enc[126:189] + '.' + enc[189:]
    _send_dns_query(server, port, enc)


def receive(s):
    data, addr = s.recvfrom(1500)
    query = _parse_dns(data)
    name = str(query.get_q().get_qname())

    return network.decode_data(name.replace('.', ''))
