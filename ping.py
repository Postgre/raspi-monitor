#!/usr/bin/python
#
# Update Raspi to blueVM communication status
# file on blueVM
#
# 

import paramiko
import sys
import time
import update_server

sample_time = time.localtime(time.time())
t = time.strftime( "%Y-%m-%d %H:%M:%S", sample_time)
command = "echo \"Last contacted by home  monitor on " + t + "\"|cat >data/link.txt"
#print "Sending command to vps: " + command
rtn = update_server.shell( command )
#print "Return from command: " + str(rtn)
