import subprocess
import time
import datetime
from datetime import date
from sys import argv
from array import array

def check_wifi_enabled_since(time):
	cmd = "adb logcat ConnectivityReceiver:D -e \'WiFi enabled 12345\'  -b main -t "+time
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out, err = proc.communicate()
	print out
	
def check_wifi_enabled(time):
	cmd = "adb logcat ConnectivityReceiver:D -e \'WiFi enabled 12345\'  -b main -T "+time
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			print output.strip()
			return int(output.strip().split()[9])
			#break
	#rc = process.poll()
	#return rc
	
def check_wifi_disabled_since(time):
	cmd = "adb logcat ConnectivityReceiver:D -e \'WiFi disabled 12345\'  -b main -t "+time
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out, err = proc.communicate()
	print out
	
def check_wifi_disabled(time):
	cmd = "adb logcat ConnectivityReceiver:D -e \'WiFi disabled 12345\'  -b main -T "+time
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			print output.strip()
			return int(output.strip().split()[9])
			#break
	#rc = process.poll()
	#return rc
	
def change_wifi_power(power):
	cmd = "ssh root@192.168.142.117 iwconfig wlan0 txpower "+str(power)
	res = subprocess.call(cmd, shell=True)	
	if (res == 0):
		print "Changed AP power to " + str(power)
	return int(time.strftime("%s", time.localtime()))	
	
def run_tcp_ping_script():
	timestamp = 0
	cmd = "adb shell su -c /data/user/0/org.qpython.qpy/files/bin/qpython-android5.sh /sdcard/45g/tcp_ping.py jepi.cs.pub.ro 1888 -i 0.1 -c 1000"
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output.strip() == '#[QPython] Press enter to exit':
			break
		if output:
			#print output.strip()
			tokens = output.strip().split()
			if (len(tokens) > 0): 
				timestamp = int(tokens[0])
			#print timestamp
	#rc = process.poll()
	#return rc
	return timestamp
	
	
def initial_timestamp():
	cmd = "adb logcat -t 1 -b main"
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out = proc.communicate()[0]
	list = out.split(" ")
	timestamp = list[0]+" "+list[1]
	return timestamp
	
dead_time_array = []	
productive_time_array = []
	
n = int(argv[1])	
	
for i in range(0,n):	
	wifi_enabled_time = 0
	last_reply_time = 0
	wifi_disabled_time = 0
	dead_time = 0
	
	initial_time = initial_timestamp()	
	print "Starting time: " + initial_time
	
	start_time = change_wifi_power(17)
	print "Wifi power changed at: " + str(start_time)

	wifi_enabled_time = check_wifi_enabled("\'"+initial_time+"\'")
	print "Wifi enabled at: " + str(wifi_enabled_time)

	start_script_time = change_wifi_power(4)
	last_reply_time = run_tcp_ping_script()
	print "Last reply at: " + str(last_reply_time)

	wifi_disabled_time = check_wifi_disabled("\'"+initial_time+"\'")
	print "Wifi disabled at: " + str(wifi_disabled_time)
	
	if (last_reply_time == 0):
		last_reply_time = wifi_enabled_time
		print "No reply"

	if (last_reply_time != 0 and wifi_disabled_time != 0 and wifi_enabled_time != 0):
		startup_time = wifi_enabled_time - start_time
		productive_time = last_reply_time - wifi_enabled_time
		dead_time = wifi_disabled_time - last_reply_time
		print "Startup time: " + str(startup_time)
		print "Productive time: " + str(productive_time)
		productive_time_array.append(productive_time)
		print "Dead time: " + str(dead_time)
		dead_time_array.append(dead_time)

print "Productive times: " + str(productive_time_array)		
print "Dead times: " + str(dead_time_array)







