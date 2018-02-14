
# from the client run: echo Hello | nc server 1888 
socat  tcp-l:1888,fork exec:'/bin/cat'


