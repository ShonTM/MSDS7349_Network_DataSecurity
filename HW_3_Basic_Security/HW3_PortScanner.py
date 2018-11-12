# -*- coding: utf-8 -*-
"""
Exercise 3.1
Jeffrey Lancon
Date 4 Nov 2018
Source: https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python
"""
# import libraries
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Input website address & return IP4 address
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports 
# Will scan ports 1-255

try:
    for port in range(1, 255):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

# Error handling statements
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Calculates the difference of time, to determine
# how long it took to run the script
t2 = datetime.now()
total = t2 - t1
print('Scanning Completed in: ', total)