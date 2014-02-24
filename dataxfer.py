#!/usr/bin/python
#
# Script to be run to save
# sensor data on server VM 199.188.100.82
# and then cause plots to be generated there

import os
import update_server

path = "/home/pi/house_monitor_files"
os.chdir( path )
update_server.upload( "t1.txt", "data/t1.txt")
update_server.upload( "t2.txt", "data/t2.txt")

update_server.shell( "bin/plot.py" )


