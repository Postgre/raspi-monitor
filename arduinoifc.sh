#!/bin/bash

cd /home/pi/house_monitor_files
echo "`date`: starting arduino interface in `pwd`" >arduinoifc.txt
while [ 1 ]
do
	echo "`date`: re.py being restarted." >>arduinoifc.txt
	./re.py
	echo "`date`: re.py exited." >>arduinoifc.txt
	sleep 30
done
