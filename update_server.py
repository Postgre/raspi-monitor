#
# module update_server
#
# Add datapoints and images to VM at 199.188.100.82

import paramiko
import sys
import time

# Catenate string (line) with formatted date, time and value to remote file
def add_dp( line, file ):

	host = '199.188.100.82'

	ssh = paramiko.SSHClient()

	# Don't require key right now
	ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())

	while True:
		try:
			ssh.connect(host, username='henry', password='jes.q.w')
			break
		except:
			print "Error on connecting: " , sys.exc_info()[0], sys.exc_info()[1]
			time.sleep(10)

	stdin, stdout, stderr = ssh.exec_command('cat >>' + file)
	stdin.write( line + "\n" )
	stdin.close()

# Add image (jpg) to directory on 199.188.100.82

def add_image( local_image, remote_image):

	host = '199.188.100.82'

	ssh = paramiko.SSHClient()

	# Don't require key right now
	ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())

	while True:
		try:
			ssh.connect(host, username='henry', password='jes.q.w')
			break
		except:
			print "Error on connecting: " , sys.exc_info()[0], sys.exc_info()[1]
			time.sleep(10)

	ftp = ssh.open_sftp()
	ftp.put( local_image, remote_image)
	ftp.close()
