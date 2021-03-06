import urllib2
import time,sys,argparse,socket,datetime
from datetime import datetime
from time import gmtime, strftime

def read_rx_bytes (card):
    return 1
    with open('/sys/class/net/'+card+'/statistics/rx_bytes', 'r') as file:
        data = file.read()
        return int(data)
 
CRLF = "\r\n\r\n"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', default = 1)
    parser.add_argument('-s', '--server', default = '141.85.241.247')
    parser.add_argument('-p', '--port', default = 80)
    parser.add_argument('-f', '--file', default = '100M')
    parser.add_argument('-c', '--count', default = 1)
    parser.add_argument('-r', dest='repeat', action='store_false')  
    parser.add_argument('-I', dest='interface')
    args = parser.parse_args()

i = 1
while i <= int(args.count): 
    before = datetime.now()
    before_wlan = read_rx_bytes('wlan0')
    before_4g = read_rx_bytes('rmnet0')
#    response = urllib2.urlopen('http://px.bot.nu/100M')
#    html = response.read(int(args.length))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    if args.interface != None: 
        s.setsockopt(socket.SOL_SOCKET, 25, args.interface + '\0')
    s.connect((args.server, int(args.port)))
    s.send("GET /%s HTTP/1.0%s" % (args.file, CRLF))
    flen = int(args.length)
    while True:
        html = (s.recv(flen))
        #print flen, len(html)
        if len(html) == flen:
            break 
        flen = flen - len(html)
    after = datetime.now()
    after_wlan = read_rx_bytes('wlan0')
    after_4g = read_rx_bytes('rmnet0')
   
    print time.time(), "Bytes:", int(args.length), "ms:", (after-before).seconds*1000.0 + (after-before).microseconds/1000.0, "Mbps:",  int(args.length)*8/( (after-before).seconds*1000000.0 + (after-before).microseconds), "wlan_rx:", after_wlan - before_wlan, "4g_rx:", after_4g - before_4g     
    
    sys.stdout.flush()
    i = i + 1
   
