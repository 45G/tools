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
no = 0

for line in f:
	data = line.split()
	if (len(data) == 8):
		data2 = data[6].split('=')
		print data2[1]
		#if (float(data2[1]) > 10):
		#	print no, " values, then  ", data2[1]
		#	no = 0
		#else:
		#	no = no+1
		#if (float(data2[1]) < 25):
		rtt.append(float(data2[1]))

print min(rtt), average(rtt), median(rtt), max(rtt), std(rtt),  "ms"
print histogram(rtt)

f.close()
