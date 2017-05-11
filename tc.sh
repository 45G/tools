# delay 
tc qdisc add dev eth0 root netem delay 97ms
#list 
tc -s qdisc
#remove 
tc qdisc del dev eth0 root netem
