#!/bin/bash
# Prepare temperature data for gnuplot, and then produce 
# temperature plot in gif file form.

/home/pi/house_monitor_files/prep-gnuplot.py \
	/home/pi/house_monitor_files/homelog.txt t1.txt t2.txt
gnuplot tempplot.gp  >temps.gif

