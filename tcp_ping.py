#!/usr/bin/env python

import time,sys,argparse 
from datetime import datetime
from socket import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length')
    parser.add_argument('-tfo', dest='tfo', action='store_true')
    parser.add_argument("destination")
    parser.add_argument("port")
    args = parser.parse_args()
    print args
    print args.tfo, args.length, args.destination, args.port


destination = args.destination
port = int(args.port) 
psize = int(args.length)  
# max 1700000 bytes for socat

while 1:

    before = datetime.now()
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((destination, port))
    sbytes = s.send((time.ctime() + 'X' * psize +  '\n').encode())
    data = s.recv(sbytes)
    rbytes = len(data)
    while rbytes < sbytes:
        #print "s= ", sbytes, "r= ", rbytes
        data = s.recv(sbytes - rbytes)
        #if data: 
        #    print data.decode()
        rbytes = rbytes + len(data)
    after = datetime.now()
    s.close()
    data = data.decode()
    print sbytes, "bytes", (after-before).seconds*1000.0 + (after-before).microseconds/1000.0, " ms"

    time.sleep(0.2)
