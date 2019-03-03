#!/usr/bin/env python3

from datetime import datetime
import ipaddress
import os

ip_range = list(ipaddress.ip_network("192.168.10.0/24")) #각자 주어진 IP 주소 대역 설정
start_time = datetime.now()

for host in ip_range[1:-1]:
	alive = os.system("ping -c 1 " + str(host) + " > /dev/null")			       
	if alive == 0:
		print(str(host) + " is up")
	else:
		print(str(host) + " is down")

end_time = datetime.now()

print("Scanning Completed in : " + str(end_time - start_time))
