#!/usr/bin/python
#
# Read one-wire temperature sensors and record temperatures
# in t1.txt anmd t2.txt
#
import w1temps
import time
import sys
import re

cnt = 0

last_t1 = 0
last_t2 = 0

delta_t = 4.0

# read temperaturs from one-wire sensors attached to Raspi
#
# Save first in file t1.txt and second in t2.txt, with date/time
# stamps like this for plotting separate lines with gnuplot:
#
#  2014-01-30 16:12:47  30.3
#  2014-01-30 16:12:52  30.5
#  2014-01-30 16:12:57  30.3
#

while True:
	try:
		line = w1temps.read_temps()
		#print 'Read line: ' + line
		m = re.search('28-.+\s+([\.\d]+)\s+28-.+\s+([\.\d]+)', line)
		if not m:
			break
		t2 = float(m.group(1))
		t1 = float(m.group(2))
		#print 'Found 2 temperatures: ' + str(t1) + ' and ' + str(t2)
		if abs( last_t1 - t1) > delta_t  or abs( last_t2 - t2) > delta_t \
			or cnt < 2 or not (cnt % 720):
			# Time sample taken
			sample_time = time.localtime(time.time())
			# Date and time for plot files
			#db_time = time.asctime( sample_time )
			# Date and time for database file
			plot_time = time.strftime( "%Y-%m-%d %H:%M:%S", sample_time)
			last_t1 = t1
			last_t2 = t2

			line = plot_time + '  ' + str(t1) + '\n'
			pout = open('t1.txt', 'a')
			pout.write( line )
			pout.close()

			line = plot_time + '  ' + str(t2) + '\n'
			pout = open('t2.txt', 'a')
			pout.write( line )
			pout.close()

	except:
		print "Exception"

	#print "Sleeping 5 seconds"
	cnt = cnt + 1;
	time.sleep(5)
