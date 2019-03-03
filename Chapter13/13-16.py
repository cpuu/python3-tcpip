#!/usr/bin/env python3

import socket

for port in range(0, 100):
	print("[+] Attempting to connect to 127.0.0.1:" + str(port))
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(("127.0.0.1", port))

	if result == 0:
		print("[+] Port " + str(port) + " is opened")
	elif result == 111:
		print("[+] Port " + str(port) + " is closed")

	sock.close()
