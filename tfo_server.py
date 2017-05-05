import socket
'''
tcp fast open server sample code
execute it before enable tfo flag

$ echo 3 | sudo tee /proc/sys/net/ipv4/tcp_fastopen
'''

PORT = 8888
TCP_FASTOPEN = 23
BUFSIZE = 1000000

def server():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_TCP, TCP_FASTOPEN, 5)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  s.bind(("", PORT))
  s.listen(1024)

  while True:
    conn, addr = s.accept()
    print 'Connection from:', addr
    bytes = 0; 
    while True:
      msg = conn.recv(BUFSIZE)
      bytes += len(msg)
      if not msg: break
      #print '+' + msg + '+'
      conn.send(msg[::-1])
      if '\n' in msg: break
    print bytes, " bytes"
    conn.close()

  s.close()

def main():
  server()

if __name__ == '__main__':
  main()
