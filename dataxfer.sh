#!/bin/bash
#
# Script to be run to take and save
# data on server VM 199.188.100.82

cd /home/pi/house_monitor_files

/home/pi/house_monitor_files/uploadfile.py t1.txt data/t1.txt
/home/pi/house_monitor_files/uploadfile.py t2.txt data/t2.txt



