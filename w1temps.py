"""
  Read onw-wire temperature sensors and return line of text with 
  sensor ID's and temperatures in F:

	28-000005b3b531 62.4866 28-000005b3bcb2 31.1

"""

import os
import re
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')

if len(device_folders) != 2:
	raise My_1wire_error

# Get device ids

device_ids = [ re.search( r"(28-[\dabcdef]+)", f ).group(1) for f in device_folders]

#  print "Device IDs: " + str(device_ids)

# Make list of device file names

files = [ f + '/w1_slave' for f in device_folders]

numdevices = len(files)

 
def _read_temp_raw( file ):
	try:
		f = open(file, 'r')
		lines = f.readlines()
		f.close()
		return lines
	except:
		print "Error opening and reading file " + file
		pass
 
def read_temps():
	tempno = 0
	ts = ""
	for file in files:
		lines = _read_temp_raw( file )
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = _read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			temp_f = temp_c * 9.0 / 5.0 + 32.0
			ts = ts + str(device_ids[tempno]) + " " + str(temp_f) + " "
		tempno = tempno + 1
        return ts
	
	
"""
print "Device ID  Temperature (F) Device ID  Temperature (F)"
while True:
	print(read_temps())	
	#time.sleep(1)
"""

