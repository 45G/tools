
wlanip=$(ip ro | grep wlan0 | awk '{print $9}')
lteip=$(ip ro | grep rmnet0 | awk '{print $9}')

if [ "x${wlanip}x" == "xx" ]; then 
echo "Please start WiFi"
exit 1
fi

if [ "x${lteip}x" == "xx" ]; then 
echo "Please start LTE"
exit 1
fi


ip rule add from $lteip table 1
ip rule add from $wlanip table 2

wlangw=$(ip route show table wlan0 | grep via | awk '{print $3}')
ltegw=$(ip route show table rmnet0 | grep via | awk '{print $3}')
wlannet=$(ip ro | grep wlan0 | awk '{print $1}')
ltenet=$(ip ro | grep rmnet0 | awk '{print $1}')

# Configure the two different routing tables
ip route add $ltenet dev rmnet0 scope link table 1
ip route add default via $ltegw dev rmnet0 table 1

ip route add $wlannet dev wlan0 scope link table 2
ip route add default via $wlangw dev wlan0 table 2

sysctl -w net.mptcp.mptcp_enabled=1

