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
	eth_rx = int(data[6])
	eth_speed = (8*eth_rx)/(time*1000)
	print time, eth_rx, eth_speed
	speed.append(eth_speed)

print min(speed), average(speed), median(speed), max(speed), std(speed), "Mbps"
print histogram(speed)

f.close()
