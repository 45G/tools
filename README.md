
* client tcp_ping.py SERVEIP PORT chunksize 
* server socat  tcp-l:1234,fork exec:'/bin/cat'

* Results from Precis 203/Ethernet

ping -i 0.1 -c 300 jepi 
rtt min/avg/max/mdev = 0.452/0.661/6.125/0.325 ms

tcp_ping.py jepi.cs.pub.ro 1234 1 
min/avg/max/mdev = 0.632/0.90/2.07/0.13 ms

ping -i 0.1 -s 1450 -c 300 jepi
rtt min/avg/max/mdev = 0.571/0.822/1.068/0.082 ms

tcp_ping.py 141.85.241.249 1234 1420
min/avg/max/mdev = 0.82/1.06/5.58/0.39 ms
