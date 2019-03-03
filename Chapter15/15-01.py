#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 10000)
print("# Starting up server")
sock.bind(server_address)

sock.listen(1)

count = 1

while True:
    connection = None
    print("\n# Waiting for a connection - " + str(count))
    try:
        connection, client_address = sock.accept()
        print("# Connection from client")
        count = count + 1

        while True:
            data = connection.recv(30)
            if data:
                print("## Received : " + data.decode("utf-8"))
                print("## Sending data back to the client")
                connection.sendall(data)
            else:
                break

    except KeyboardInterrupt:
        print("\n## Interrupt received, stopping...")
        break

    finally:
        print("## Connection closed")
        if connection:
            connection.close()

sock.shutdown(socket.SHUT_RDWR)
sock.close()
print("# Server terminated\n")
