#!/usr/bin/python
#
# Read arduino output on USB serial poprt, record temperatures
# in homelog.txt, t1.txt anmd t2.txt
#
import time
import sys
import re
import serial

cnt = 0

last_t1 = 0
last_t2 = 0

delta_t = 4.0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
# read temperatured from Arduino
#
# Save first in file t1.txt and second in t2.txt, with date/time
# stamps like this for plotting separate lines with gnuplot:
#
#  2014-01-30 16:12:47  30.3
#  2014-01-30 16:12:52  30.5
#  2014-01-30 16:12:57  30.3
#

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
				# Time sample taken
				sample_time = time.localtime(time.time())
				# Date and time for plot files
				#db_time = time.asctime( sample_time )
				# Date and time for database file
				plot_time = time.strftime( "%Y-%m-%d %H:%M:%S", sample_time)
				last_t1 = t1
				last_t2 = t2
				line = plot_time + '  ' + str(t1) + '\n'
				#print l
				pout = open('t1.txt', 'a')
				pout.write( line )
				pout.close()
				line = plot_time + '  ' + str(t2) + '\n'
				#print l
				pout = open('t2.txt', 'a')
				pout.write( line )
				pout.close()
			break
		except:
			print "Exception"
			pass
	cnt = cnt + 1;

