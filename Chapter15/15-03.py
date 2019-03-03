#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 10000)

try:
    print("# Connecting to server...")
    sock.connect(server_address)

    message = b"This is the message."
    print("## Sent     : " + message.decode("utf-8"))
    sock.sendall(message)

    data = sock.recv(30)
    print("## Received : " + data.decode("utf-8"))

except socket.error:
    print("# Cannot connect to server.")

finally:
    print("# Closing socket")
    sock.close()
