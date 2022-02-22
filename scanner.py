#!/bin/python3

import sys #allows us to enter command line args, amoung other things
import socket
from datetime import datetime

#Define our target
#python3 scanner.py <ip>
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translates host name to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit() #if it is done wrong, this will exit the program for us 
    

#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
                      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                      socket.setdefaulttimeout(1) #is a float
                      result = s.connect_ex((target,port))
                      #returns error indicator, if no error returns 0
                      print("Checking port {}".format(port))
                      if result == 0:
                          print("Port {} is open".format(port))
                      s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()























































