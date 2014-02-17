#!/usr/bin/python
#
# Test module update_server
#
# Add line of text and image to files on VM at 199.188.100.82

import paramiko
import sys
import update_server

if len(sys.argv) != 5:
	print "Use: add_dp_t.py line file image file"
	sys.exit()

line, datafile, image, imagefile = sys.argv[1:5]

update_server.add_dp( line, datafile )

update_server.add_image( image, imagefile)
