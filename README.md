Exfil
=====

Overview
--------
Exfil is a tool designed to exfiltrate data using various techniques, which allows a security team to test whether its monitoring system can effectively catch the exfiltration. The idea for Exfil came from a Twitter conversation between @averagesecguy, @ChrisJohnRiley, and @Ben0xA and was sparked by the TrustWave POS malware whitepaper available at https://gsr.trustwave.com/topics/placeholder-topic/point-of-sale-malware/.


###Workflow
1. A tester starts up a listener on one side of the monitoring system, specifying the exfiltration method.
2. The tester then starts up a sender on the other side of the monitoring system, specifying the data to transmit and the exfiltration method.
3. The sender then transmits the specified data to the listener while the tester attempts to see the data exfiltration using the monitoring system.


Modules
-------
* `dns_lookup` - Transmit data using DNS lookups as described here http://breenmachine.blogspot.ca/2014/09/transfer-file-over-dns-in-windows-with.html
* `ping_data` - Transmit data using ICMP ping packets with data as defined here http://blog.c22.cc/2012/02/17/quick-post-fun-with-python-ctypes-simpleicmp/


Options
-------
* `-d string` - Send a string of data.
* `-f filename` - Send the specified file.
* `-l port` - Listen for a connection on the specified port. If no port is give then use the default port for the module.
* `-m module_name` - Transmit data using the specified module.
* `-s server[:port]` - Server where data should be sent. If no port is specified, then use the default port for the module.


Usage
-----
Start a listener: exfil -l <port> -m module_name
Send a string of data: exfile -s server[:port] -d String_of_data -m module_name
Send a file: exfil -s server[:port] -f file_to_send -m module_name