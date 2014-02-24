#!/usr/bin/python
#
# Upload file to VM server at 199.188.100.82
#
# 

import paramiko
import sys
import update_server

if len(sys.argv) != 3:
	print "Use: uploadfile.py local_file remote_file"
	sys.exit()

lf, rf = sys.argv[1:3]

update_server.upload( lf, rf)
