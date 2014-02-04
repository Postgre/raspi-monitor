#!/bin/bash

cd /home/pi/house_monitor_files
echo "`date`: starting arduino interface in `pwd`" >arduinoifc.txt
while [ 1 ]
do
	echo "`date`: re-plot.py being restarted." >>arduinoifc.txt
	./re-plot.py
	echo "`date`: re-plot.py exited." >>arduinoifc.txt
	sleep 30
done
