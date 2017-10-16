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
	if (len(data) == 8 and data[7]=='Mbits/sec'):
		speed.append(float(data[6]))

print min(speed), average(speed), median(speed), max(speed), std(speed),  "Mbps"
print histogram(speed)

f.close()