#each request is one word which is passed to dd as a count of 1MB blocks to generate
#useful for speed testing
# from client, run: echo '12' |  nc server 1888  | wc -c
PORT=1888
echo listening on port $PORT 
socat  tcp-l:$PORT,fork exec:'sh -c "{ while read x; do dd if=/dev/zero bs=1000000 count=$x; done; } " '
