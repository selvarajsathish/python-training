"""
Server will send response to client by vlidationg the host authentication and file availablity
"""

import socket
import re
import os

h_list = ['vvsa-hp-elitebook-745-g2','vvsa-hp-elitebook-745-g3']
f_list = ['index.html','open.php','text.json']

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
host = socket.gethostname()
s.bind((host,8080))
s.listen(5)
conn,addr = s.accept()
print ("connected by",addr)
while True:
	data = conn.recv(16240)
	if not data:
		break
	else:
		host = re.search(r'(Host: (.*)g2)',data)
		h = host.group().lstrip('Host: ')
		if h in h_list:
			print "client authenticated"
			file = re.search(r'GET (.*)html',data)
			f = file.group().lstrip('GET /')
			if f in f_list:
				s = os.stat(f).st_size
				conn.send("HTTP/1.1 200 OK\nContent-Type: text/plain\nContent-Length: " + str(s) + "\n\n" + f +"")
			else:
				conn.send('File not found')
		else:
			conn.send('Client dont have permission')				
conn.close()


