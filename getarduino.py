#!/usr/bin/python
import time
import sys
import re
import serial

cnt = 0
temps = []


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
line = ser.readline() # Arduino sends line of text every 5 seconds
localtime = time.asctime( time.localtime(time.time()) )
l = localtime + ': ' + line.rstrip()
print "Content-type: text/html\n\n"
print "<h1>Zouck House Status</h1>"
print "<p>" + l + "</p>"

