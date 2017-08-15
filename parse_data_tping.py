#!/usr/bin/env python

import sys
from math import sqrt

def stddev(lst):
    mean = float(sum(lst)) / len(lst)
    return sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, lst))) / len(lst))

f = open(sys.argv[1])

rtt = []

for line in f:
	data = line.split()
	rtt.append(float(data[4]))

print min(rtt), sum(rtt)/len(rtt), max(rtt), stddev(rtt), "ms"

f.close()
