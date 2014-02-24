#!/usr/bin/python
#
# Script run by cron to take and save
# photo in /home/pi/house_monitor_files/images/current_image.jpg
# and send to VPS server under name composed with date string.

import os
import time
import update_server

sample_time = time.localtime(time.time())

remotefilename = "image_" + time.strftime( "%Y-%m-%d_%H:%M:%S", sample_time) + ".jpg"
remotepathname = "images/" + remotefilename

#print "Filename: " + remotefilename

localpathname = "/home/pi/house_monitor_files/images/current_image.jpg"

os.system("raspistill -vf -hf -w 300 -h 300 -o " + localpathname)

# print "Uploading file: " + localpathname + " to VPS as " + remotepathname
update_server.upload( localpathname,  remotepathname)

# Link this image to current_image
update_server.shell( "rm images/current_image.jpg;ln -s " + remotefilename + " images/current_image.jpg")
