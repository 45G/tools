
* client tcp_ping.py SERVEIP PORT chunksize 
* server socat  tcp-l:1234,fork exec:'/bin/cat'
* serverul socat adds 2ms to the response, when compared with a python server (tfo_server.py)
* TFO 
  ** on server sysctl -w net.ipv4.tcp_fastopen=2
  ** on client sysctl -w net.ipv4.tcp_fastopen=1
  ** tfo_server.py 
  ** tfo_client.py 


* Results from Precis 203/Ethernet; socat server + old version of tcp_ping, which keeps connection open and measures RTT for write and echo

  ** ping -i 0.1 -c 300 jepi 
      rtt min/avg/max/mdev = 0.452/0.661/6.125/0.325 ms

  ** tcp_ping.py jepi.cs.pub.ro 1234 1 
      min/avg/max/mdev = 0.632/0.90/2.07/0.13 ms

  ** ping -i 0.1 -s 1450 -c 300 jepi
      rtt min/avg/max/mdev = 0.571/0.822/1.068/0.082 ms

  ** tcp_ping.py 141.85.241.249 1234 1420
      min/avg/max/mdev = 0.82/1.06/5.58/0.39 ms

* results from Precis 203/Eth
  ** python ./tcp_ping.py -l 2 141.85.241.250 1888
     avg = 1.66 ms 
  ** python ./tfo_client.py
     avg = 1.05 ms

* results from Precis 203/WiFi S7, tfo_server 
  ** maintain ping -i 0.01 to AP! 
  ** tcp_ping.py -l 2 141.85.241.250 1888
     avg = 8.7ms
  ** ping 
     avg = 3.1ms 
  ** tfo_client.py
     avg = 3.74ms 
