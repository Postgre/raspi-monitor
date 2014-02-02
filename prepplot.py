#!/usr/bin/python
import re

t0 = []
t1 = []

fd = open("/home/pi/house_monitor_files/homelog.txt", 'r');
for line in fd:
	# print "We read: " + line
	m = re.match( r'.+\s([\.\d]+)\s+and\s+([\.\d]+)', line)
	if ( m != None):
		t0.append(m.group(1))
		t1.append(m.group(2))
		"""
		print "T1: " + m.group(1)
		print "T2: " + m.group(2)
		"""
	else:
		print "No match."

fd.close()

n = 1
for t in t0:
	print( str( n ) + " " + t )
	n = n + 1
print "\n"
n = 0
for t in t1:
	print( str( n ) + " " + t )
	n = n + 1

