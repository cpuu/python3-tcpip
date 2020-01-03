#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 10000)

try:
    print("#Connecting to server..")
    sock.connect(server_address)

    for length in range(1, 40):
        message = b"A" * length
        print("Try #" + str(length))
        print("message : " + message.decode("utf-8"))

        sock.sendall(message)

        recv_data = sock.recv(length)

        if len(recv_data) == len(message):
            print("Pass!")
        else:
            print("An Error Has Occurred!!!")
            print("The server seems to have a buffer size of " + str(len(recv_data)))
            break

except socket.error:
    print("#Cannot connect to server.")

finally:
    print("#Closing socket")
    sock.close()
