import time,sys 
from datetime import datetime
from socket import *

s = socket(AF_INET, SOCK_STREAM)
if len(sys.argv) <= 1:
    destination = "jepi.cs.pub.ro"
else:
    destination = sys.argv[1]

if len(sys.argv) <= 2:
    port = 1234
else:
    port = sys.argv[2]

if len(sys.argv) <= 3:
    psize = 1
else:
    psize = int(sys.argv[3])

s.connect((destination, 1234))

while 1:
    before = datetime.now()
    s.send((time.ctime() + 'X' * psize +  '\n').encode())
    data = s.recv(4096)
    after = datetime.now()
    data = data.decode()
    print (after-before).seconds*1000.0 + (after-before).microseconds/1000.0, "ms"

    time.sleep(0.2)
