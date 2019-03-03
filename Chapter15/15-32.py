#!/usr/bin/env python3

from scapy.all import *
import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 10000))

fuzz_stream = StreamSocket(sock)
scapy_packet = IP(dst="127.0.0.1")/TCP(dport=10000)/fuzz(Raw())

print(fuzz_stream.send(scapy_packet))

sock.close()
