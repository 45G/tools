from sys import argv
import csv

reset = 0
power_change = 0
wifi_disable_timeout = 0

with open(argv[1], 'rb') as f1_input:
	for row in csv.reader(f1_input, delimiter=' ', skipinitialspace=True):
		if (len(row) > 0):
			if (row[0] == 'Experiment:'):
				print '\n' + ' '.join(row)
				power_change = 0
			if (row[0] == 'Startup' or row[0] == 'Productive' or row[0] == 'Dead'):
				print ' '.join(row)
			if (row[0] == 'Reset'):
				print ' '.join(row)
				reset = reset+1
				if (power_change == 1):
					wifi_disable_timeout = wifi_disable_timeout + 1
		if (len(row) > 6):
			if (row[2] == 'changed' and (row[4] == '4' or row[4] == '3' or row[4] == '2' or row[4] == '1')):
				print ' '.join(row)
				power_change = 1
				
print 'Experiment was reset ' + str(reset) + ' times\n Wifi disabled timeout ' + str(wifi_disable_timeout) + ' times'