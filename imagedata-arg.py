#!/usr/bin/python
# 
# Get date and length of image file
import os
import re
import sys

if len(sys.argv) != 2:
	print "Use: plotrange.py filename"
	sys.exit(1)

filename = sys.argv[1]

result =  os.popen("ls -ltr " + filename ).read()
#print "Command result: " + result
match = re.search( r"\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+\s+\S+\s+\S+)\s+\S+", result)
if match:
	size =  str(match.group(1))
	date =  str(match.group(2))
	print "<p><center>Image size: " + size + "  Captured on: " + date + "</center></p>"

