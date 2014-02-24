#!/bin/bash

cd /home/pi/house_monitor_files
echo "`date`: starting 1wire temperature sensor interface in `pwd`" >>1wiretemp.txt
# Do the following in /etc/modules:
#sudo modprobe w1_gpio
#sudo modprobe w1_therm
while [ 1 ]
do
	echo "`date`: re-plot-w1.py being started." >>1wiretemp.txt
	./1wiretemps.py
	echo "`date`: re-plot-w1.py exited." >>1wiretemp.txt
	sleep 30
done
