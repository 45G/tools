#!/usr/bin/env python

import sys
from math import sqrt

def stddev(lst):
    mean = float(sum(lst)) / len(lst)
    return sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, lst))) / len(lst))

f = open(sys.argv[1])

speed = []

for line in f:
	data = line.split()
	time = float(data[4])
	wlan_rx = int(data[6])
	lte_rx = int(data[8])
	print time, wlan_rx, lte_rx, wlan_rx/time, lte_rx/time, (wlan_rx + lte_rx)/time
	speed.append((wlan_rx + lte_rx)/time)


print min(speed)/1000, sum(speed)/len(speed)/1000, max(speed)/1000, stddev(speed)/1000, "MBytes/s"
print 8*min(speed)/1000, 8*sum(speed)/len(speed)/1000, 8*max(speed)/1000, 8*stddev(speed)/1000, "Mbps"

f.close()
