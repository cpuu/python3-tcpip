#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("192.168.10.213")
print(ftp.getwelcome())
ftp.login(user="odj", passwd = "1234")

lists = []
ftp.dir(lists.append)
for line in lists:
	print(line)

ftp.quit()
