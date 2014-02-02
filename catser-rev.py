#!/usr/bin/python
import time
import sys
import re
import serial

cnt = 0
temps = []


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
while 1:
	line = ser.readline() # Arduino sends line of text every 5 seconds
	if cnt < 50 or 0 == (cnt % 720):    # This goes thru every 60 minutes, after 50 readings
		localtime = time.asctime( time.localtime(time.time()) )
		l = localtime + ': ' + line.rstrip()
		temps.insert(0,l)
		if len( temps) > 50:
			temps.pop()
		pout = open('homelog.txt', 'w');
		pout.write('Last 50 temperature measurements:\n\n')
		for ln in temps:
			pout.write( ln + '\n')
		pout.close()
	cnt = cnt + 1;

