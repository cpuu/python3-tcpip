#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 22))
sock.send(("Scanning Port...").encode())

result = sock.recv(1024)
print(result)
