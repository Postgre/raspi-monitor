#!/usr/bin/python
import time
import sys
import re
import serial

cnt = 0

last_t1 = 0
last_t2 = 0

delta_t = 4.0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
while 1:
	
	while True:
		try:
			line = ser.readline().rstrip() # Arduino sends line of text every 5 seconds
			#print 'Read line: ' + line
			m = re.search('([\.\d]+)\s+([\.\d]+)', line)
			if not m:
				break
			t1 = float(m.group(1))
			t2 = float(m.group(2))
			#print 'Found 2 temperatures: ' + str(t1) + ' and ' + str(t2)
			if abs( last_t1 - t1) > delta_t  or abs( last_t2 - t2) > delta_t \
				or not (cnt % 720):
				localtime = time.asctime( time.localtime(time.time()) )
				last_t1 = t1
				last_t2 = t2
				l = localtime + ': ' + str(t1) + ' and ' + str(t2) + '\n'
				#print l
				pout = open('homelog.txt', 'a')
				pout.write( l )
				pout.close()
			break
		except:
			print "Exception"
	cnt = cnt + 1;

