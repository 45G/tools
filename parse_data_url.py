#!/usr/bin/env python

import sys
from math import sqrt
from numpy import median
from numpy import average
from numpy import mean
from numpy import std
from numpy import histogram

f = open(sys.argv[1])

speed = []

for line in f:
	data = line.split()
	time = float(data[4])
	wlan_rx = int(data[6])
	lte_rx = int(data[8])
	wlan_speed = (8*wlan_rx)/(time*1000)
	lte_speed = (8*lte_rx)/(time*1000)
	total_speed = wlan_speed + lte_speed
	print time, wlan_rx, lte_rx, wlan_speed, lte_speed, total_speed
	speed.append(total_speed)

print min(speed), average(speed), median(speed), max(speed), std(speed), "Mbps"
print histogram(speed)


f.close()
