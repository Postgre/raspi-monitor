#!/bin/bash
#
# Script to be run by www-data user cron to take and save
# photo in /var/www/data so it is available from web site.

remotefilename="image_`date +%Y-%m-%d_%H:%M:%S`.jpg"

localpathname="/home/pi/house_monitor_files/images/current_image.jpg"

raspistill -vf -hf -w 300 -h 300 -o $localpathname

/home/pi/house_monitor_files/uploadfile.py $localpathname  images/$remotefilename
