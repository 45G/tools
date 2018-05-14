import subprocess
import time
import datetime
from datetime import date
from sys import argv, stdout
from array import array
import os
import signal
from threading import Timer
from threading import Thread



def reset_exp():
	cmd = "ssh root@192.168.142.117 \'ip link set dev wlan0 down && /etc/init.d/hostapd stop && /etc/init.d/hostapd start\'"
	res = subprocess.call(cmd, shell=True)	
	if (res == 0):
		print "Reset experiment"
	#return int(time.strftime("%s", time.localtime()))
	
def cancel_exp(reason):
	change_wifi_power(1)
	time.sleep(5)
	print "Experiment canceled due to: " + reason
	
	
def check_wifi_enabled(time, timeout):
	timestamp = 0
	cmd = "timeout "+str(timeout)+" adb logcat ConnectivityReceiver:D -e \'WiFi enabled 12345\'  -b main -T "+time
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			print output.strip()
			timestamp = int(output.strip().split()[9])
			break
	try:
		os.killpg(os.getpgid(process.pid), signal.SIGKILL)
	except:
		pass
	return timestamp
			
	
	
def check_wifi_disabled(time, timeout):
	timestamp = 0
	cmd = "timeout "+str(timeout)+" adb logcat ConnectivityReceiver:D -e \'WiFi disabled 12345\'  -b main -T "+time
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			print output.strip()
			timestamp = int(output.strip().split()[9])
			break
	try:
		os.killpg(os.getpgid(process.pid), signal.SIGKILL)
	except:
		pass
	return timestamp
	
def change_wifi_power(power):
	cmd = "ssh root@192.168.142.117 iwconfig wlan0 txpower "+str(power)
	res = subprocess.call(cmd, shell=True)	
	if (res == 0):
		print "Changed AP power to " + str(power)
	return int(time.strftime("%s", time.localtime()))	
	
def run_tcp_ping_script():
	global timestamp 
	timestamp = 0
	cmd = "adb shell su -c /data/user/0/org.qpython.qpy/files/bin/qpython-android5.sh /sdcard/45g/tcp_ping.py jepi.cs.pub.ro 1888 -i 0.01 -c 10000"
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output.strip() == '#[QPython] Press enter to exit':
			break
		if not output:
			break
			
		#print output
		tokens = output.strip().split()
		if (len(tokens) == 0):
			break
			
		#print "lala", tokens[0]
		try:
			timestamp = int(tokens[0])
			print output,
			stdout.flush()
		except:
			print output
			#for l in process.stdout.readline():
			#	print output
			break

	os.killpg(os.getpgid(process.pid), signal.SIGKILL)
	#return timestamp
	
	
def get_timestamp():
	cmd = "adb logcat -t 1 -b main"
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out = proc.communicate()[0]
	list = out.split(" ")
	if (len(list)<2):
		print "Error parsing logcat " + out
		return None
	else:	
		timestamp = list[0]+" "+list[1]
		return timestamp

	
dead_time_array = []	
productive_time_array = []
	
n = int(argv[1])	

reset_exp()
	
for i in range(0,n):	
	wifi_enabled_time = 0
	last_reply_time = 0
	wifi_disabled_time = 0
	dead_time = 0
	
	print "Experiment: " + str(i + 1)
	
	initial_time = get_timestamp()	
	if (initial_time == None):
		reset_exp()
		continue
	print "Starting time: " + initial_time
	
	stdout.flush()
	
	start_time = change_wifi_power(17)
	print "Wifi power changed to 17 at: " + str(start_time)
	
	stdout.flush()

	wifi_enabled_time = check_wifi_enabled("\'"+initial_time+"\'", 900)
	if (wifi_enabled_time == 0):
		reset_exp()
		continue
	print "Wifi enabled at: " + str(wifi_enabled_time)

	stdout.flush()
	
	initial_time = get_timestamp()
	if (initial_time == None):
		reset_exp()
		continue
	
	power5_time = change_wifi_power(5)
	print "Wifi power changed to 5 at: " + str(power5_time)
	
	stdout.flush()
	
	thread = Thread(target=run_tcp_ping_script)
	thread.start()
	
	#last_reply_time = run_tcp_ping_script()
	
	
	time.sleep(20)
	
	power4_time = change_wifi_power(4)
	print "Wifi power changed to 4 at: " + str(power4_time)
	
	time.sleep(20)
	
	power3_time = change_wifi_power(3)
	print "Wifi power changed to 3 at: " + str(power3_time)
	
	time.sleep(20)
	
	power2_time = change_wifi_power(2)
	print "Wifi power changed to 2 at: " + str(power2_time)
	
	time.sleep(20)
	
	power1_time = change_wifi_power(1)
	print "Wifi power changed to 1 at: " + str(power1_time)
	
	thread.join()
	last_reply_time = timestamp
	
	stdout.flush()
	
	print "Last reply at: " + str(last_reply_time)
	
	stdout.flush()

	wifi_disabled_time = check_wifi_disabled("\'"+initial_time+"\'", 900)
	if (wifi_disabled_time == 0):
		reset_exp()
		continue
	
	stdout.flush()
		
	print "Wifi disabled at: " + str(wifi_disabled_time)
	
	stdout.flush()
	
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
	
	stdout.flush()
	time.sleep(5)

print "Productive times: " + str(productive_time_array)		
print "Dead times: " + str(dead_time_array)







