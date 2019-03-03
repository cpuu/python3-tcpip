#!/usr/bin/env python3

import os
import socket
from struct import *

os.system("ifconfig eth0 promisc")

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

data = s.recv(65565)

#IP Header
ip_header = data[0:20]
ip_header = unpack("!BBHHHBBH4s4s", ip_header)

version_ip_header_length = ip_header[0]
version = version_ip_header_length >> 4
ip_header_length = version_ip_header_length & 0xF
ip_header_length = ip_header_length * 4
ttl = ip_header[5]
protocol = ip_header[6]
ip_source_address = socket.inet_ntoa(ip_header[8])
ip_destination_address = socket.inet_ntoa(ip_header[9])

print("IP Header")
print("Version:", str(version))
print("IP Header Length:", str(ip_header_length))
print("TTL:", str(ttl))
print("Protocol:", str(protocol))
print("Source IP Address:", str(ip_source_address))
print("Destination IP Address:", str(ip_destination_address))
print()

#ICMP Header
icmp_header = data[ip_header_length:ip_header_length + 8]
icmp_header = unpack("!BBHHH", icmp_header)

type = icmp_header[0]
code = icmp_header[1]
checksum = icmp_header[2]
id = icmp_header[3]
seq = icmp_header[4]

print("ICMP Header")
print("Type:", str(type))
print("Code:", str(code))
print("Checksum:", str(checksum))
print("ID:", str(id))
print("Sequence:", str(seq))
print()

#ICMP Payload
icmp_header_length = 8
header_size = ip_header_length + icmp_header_length
payload_data_size = len(data) - header_size
icmp_payload_data = data[header_size:]

print("ICMP Payload")
print("Payload Data:", str(icmp_payload_data))
print()
