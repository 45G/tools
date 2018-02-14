
# filename should be an integer
# from the client, run: curl http://px.bot.nu/50
#
socat \
    -d -d \
    TCP-LISTEN:80,crlf,reuseaddr,fork \
    SYSTEM:"
	read request 
        echo HTTP/1.1 200 OK; 
        echo Content-Type\: text/plain; 
        echo; 
        echo \"Server: \$SOCAT_SOCKADDR:\$SOCAT_SOCKPORT\";
        echo \"Client: \$SOCAT_PEERADDR:\$SOCAT_PEERPORT\";
	cnt=\$(echo \$request | awk '{print \$2}' | tr -d '\/' );
	#echo \"cnt= \$cnt\"
     	dd if=/dev/zero bs=1M count=\$cnt
        echo \"$(date)\"; 
    "
