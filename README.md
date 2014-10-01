Exfil
=====

Overview
--------
Exfil is a tool designed to exfiltrate data using various techniques, which allows a security team to test whether its monitoring system can effectively catch the exfiltration. The idea for Exfil came from a Twitter conversation between @averagesecguy, @ChrisJohnRiley, and @Ben0xA and was sparked by the TrustWave POS malware whitepaper available at https://gsr.trustwave.com/topics/placeholder-topic/point-of-sale-malware/.


###Workflow
1. A tester starts up a listener on one side of the monitoring system, specifying the exfiltration method.
2. The tester then starts up a sender on the other side of the monitoring system, specifying the data to transmit and the exfiltration method.
3. The sender then transmits the specified data to the listener while the tester attempts to see the data exfiltration using the monitoring system.


Prerequisites
-------------
* `dnslib` - pip install dnslib
* `dpkt` - Download the source code from [Google Code](https://code.google.com/p/dpkt/downloads/detail?name=dpkt-1.8.tar.gz). Once dowloaded extract the tar file and run `python setup.py install`


Modules
-------
* `dns_lookup` - Transmit data using DNS lookups as described here http://breenmachine.blogspot.ca/2014/09/transfer-file-over-dns-in-windows-with.html
* `ping_data` - Transmit data using ICMP ping packets with data as defined here http://blog.c22.cc/2012/02/17/quick-post-fun-with-python-ctypes-simpleicmp/


Usage
-----
```
usage: exfil.py [-h] (-d string | -f filename) (-l | -s server) [-p port] module_name

Exfiltrate data.

positional arguments:
  module_name  Exfiltration module to use.

optional arguments:
  -h, --help   show this help message and exit
  -d string    String of data to exfiltrate.
  -f filename  File to send.
  -l           Listen for a connection.
  -s server    Server where data should be sent. Can be a hostname
  or an IP address.
  -p port      Port to use when listening or connecting.
```

Examples
--------
Start a listener: exfil -l <port> -m module_name
Send a string of data: exfile -s server[:port] -d String_of_data -m module_name
Send a file: exfil -s server[:port] -f file_to_send -m module_name
