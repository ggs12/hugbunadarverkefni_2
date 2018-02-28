#!/usr/bin/env python
import socket
import subprocess
import sys
import random
#import threading
import time
from datetime import datetime
#from threading import Timer

PORTS = [20,21,22,23,25,69,152,989,990,830,107,992,465,587,53,90,80,135,853,5353,67,68,546,547,647,847,8080]


def randportslist(numb):
    old = None;
    while True:
        index = random.randrange(len(numb))
        if index  != old:
            yield numb[index]
            old = index;

# Clear the screen
subprocess.call('clear', shell=True)
tala = 0
talaend = 250

#portbegin = (int(input("Enter the number of ports to begin scanning from: ")))
#portend = (int(input("Enter the number of ports to scan end scan at: ")))

#remoteServer    = (raw_input("Enter a remote host to scan: "))


interestingPorts = random.shuffle(PORTS);

remoteServer    = str(input("Enter the IP address to scan at: "));
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in PORTS:
        t3 = datetime.now()
        if (port % 10 == 0):
            runtimeVariable = t3-t1
            #print ("-" * 60)
            #print ("slight delay", port ,": ports scanned in time of : ", runtimeVariable , " seconds ")
            #print ("-" * 60)
            time.sleep(0.3) # I was hoping thi would make the program harder to detect but it doesnt seem to do much
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

#socket.socket

    #192.168.56.1/24 brd 192.168.56.255
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)
