#!/usr/bin/env python

import sys
from math import sqrt
from numpy import median
from numpy import average
from numpy import mean
from numpy import std
from numpy import histogram

f = open(sys.argv[1])

rtt = []

for line in f:
	data = line.split()
	if (float(data[4]) < 140):
		rtt.append(float(data[4]))

print min(rtt), average(rtt), median(rtt), max(rtt), std(rtt),  "ms"
print histogram(rtt, bins=20)

f.close()
