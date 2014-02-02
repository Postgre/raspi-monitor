#!/usr/bin/python
#
# Use:
#
#   $ python prep-gnuplot.py input_temp_file t1_output_file t2_output_file
#
import sys
import re
from datetime import datetime

# Check arguments
if (not len(sys.argv) == 4):
	print "Use: python prep-gnuplot.py tin  t1out t2out"
	exit

tinfile = sys.argv[1]
t1ofile = sys.argv[2]
t2ofile = sys.argv[3]

"""
Prepare temperature files for gnuplot
"""
t0 = []
t1 = []

fd = open(tinfile, 'r');
for line in fd:
	# print "We read: " + line
	# decode times in homelog.tx like "Thu Jan 30 16:13:02 2014:"
	# and two temperatures like "d.d"
	m = re.match( r'(.+):\s+([\.\d]+)\s+and\s+([\.\d]+)', line)
	if ( m != None):
		time = datetime.strptime(m.group(1),"%a %b %d %H:%M:%S %Y")
		t0.append(str(time) + "  " + m.group(2))
		t1.append(str(time) + "  " + m.group(3))
		"""
		print "Time: " + str(time)
		print "T1: " + m.group(2)
		print "T2: " + m.group(3)
		"""
	else:
		print "No match."

fd.close()
fd = open(t1ofile, 'w');
for t in t0:
	fd.write( t + "\n")
fd.close()
fd = open(t2ofile, 'w');
for t in t1:
	fd.write( t + "\n")
fd.close()

