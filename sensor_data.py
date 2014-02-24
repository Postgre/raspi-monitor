#
# module sensor_data
#
# Use in Raspi to send pings and data to VPS
# via UDP datagrams
#
# Use house_server_full.py on VPS ro
# match this module output
#
# Use:
#  import sensor_data
#  import time
#
#  while 1:
#        sensor_data.ping()
#        sensor_data.send_dps( [["cvb444", str(time.time()), 69.4]])
#        sensor_data.send_dps( [ ["cvb444", str(time.time()), 69.4],
#                ["cvb437", str(time.time()), 45.4],
#                ["cvb438", str(time.time()), 45.4],
#                ["cvb439", str(time.time()), 45.4]])
#        time.sleep(5)
#
import socket

#host = "199.188.100.82"
host = "www.zouck.org"
port = 1024                # The port for sensor data server
#port = 1025

print "UDP target IP:", host
print "UDP target port:", port

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Send multiple sensor updates in same datagram
# dps is list of lists of tuples sensor id, time, value

def send_dps( dps ):
	for dp in dps:
		id, t, value = dp
		sock.sendto( "data " + str(id) + " " + str(t) + " " + 
			str(value), (host, port))

def ping():
	sock.sendto("ping", (host, port))
