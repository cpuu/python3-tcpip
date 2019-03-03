#!/usr/bin/env python3

import socket
import errno
import sys

ip = "127.0.0.1"
port = 21
username = "root"
password = "toor"

command_list = ["ABOR", "ACCT", "ADAT", "ALLO", "APPE", "AUTH", "CCC", "CDUP", "CONF", "CWD", "DELE", "ENC", "EPRT", "EPSV", "FEAT", "HELP", "LANG", "LIST", "LPRT", "LPSV", "MDTM", "MIC", "MKD", "MLSD", "MLST", "MODE", "NLST", "NOOP", "OPTS", "PASV", "PBSZ", "PORT", "PROT", "PWD", "REIN", "REST", "RETR", "RMD", "RNFR", "RNTO", "SITE", "SIZE", "SMNT", "STAT", "STOR", "STOU", "STRU", "SYST", "TYPE", "XCUP", "XMKD", "XPWD", "XRCP", "XRMD", "XRSQ", "XSEM", "XSEN"]

for command in command_list:
    for length in range(2000, 5000, 100):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.recv(1024)

            msg = "USER " + username + "\r\n"
            sock.send(msg.encode())
            sock.recv(1024)
            msg = "PASS " + password + "\r\n"
            sock.send(msg.encode())
            sock.recv(1024)

            fuzz = "A" * length
            msg = command + " " + fuzz + "\r\n"
            print("Fuzzing " + command + " with length: " + str(len(msg)))
            sock.send(msg.encode())
            sock.settimeout(5.0)
            result = sock.recv(1024)
            sock.settimeout(None)
            print(result.decode("utf-8"))

            msg = "QUIT\r\n"
            sock.send(msg.encode())
            sock.close()

        except socket.error as serr:
            if serr.errno == errno.ECONNREFUSED:
                print("vsFTPd is not currently working...")
                sys.exit()

            else:
                print("Failed to connect to ftp : "+ str(serr))
                print("An Error Has Occurred with buffer length : " + str(length))

            break
