import numpy as np
import matplotlib.pyplot as plt
from sys import argv

with open('../data/dead_time'+argv[1]+'.txt','r') as f:
	data = f.read()
	data = data.split(', ')
	data = map(int, data)
	print "Median " + str(np.median(data))
	print "Mean " + str(np.mean(data))
	print "Min " + str(np.min(data))
	print "Max " + str(np.max(data))
	median = np.median(data)/10
	bins = np.array([0,10,20,30,40,1010])
	
	hist, bin_edges = np.histogram(data,bins)
	fig,ax = plt.subplots()

	# Plot the histogram heights against integers on the x axis
	ax.bar(range(len(hist)),hist,width=1,color = "darkturquoise",edgecolor='cadetblue', label=hist) 

	# Set the ticks to the middle of the bars
	ax.set_xticks([0.5+i for i,j in enumerate(hist)])

	# Set the xticklabels to a string that tells us what the bin edges were
	ax.set_xticklabels(['{} - {}'.format(bins[i],bins[i+1]) for i,j in enumerate(hist)])
	
	ax.axvline(x=median,color='r', linestyle='--')
	
	j = 0
	for i in ax.patches:
		ax.text(i.get_x()+.4, i.get_height()-14, hist[j], fontsize=10, color='black')
		j = j + 1
	
	plt.xlabel('Dead time (s)') 
	plt.ylabel('Count')
	plt.text(median+0.1, 50, str(np.median(data)), color='red')
	plt.savefig('../data/dead_time'+argv[1]+'.png')