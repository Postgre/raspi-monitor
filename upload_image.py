#!/usr/bin/python
#
# Upload image file to VM server at 199.188.100.82
#
# 

import paramiko
import sys
import update_server

if len(sys.argv) != 3:
	print "Use: upload_image.py local_image remote_image"
	sys.exit()

image, imagefile = sys.argv[1:3]

update_server.add_image( image, imagefile)
