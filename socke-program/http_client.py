"""
client will send http request for particular web file

"""
import socket

c = socket.socket()
host = socket.gethostname()
c.connect((host,8080))
# while True:
c.send("GET /index.html HTTP/1.1\nHost: vvsa-hp-elitebook-745-g2:8080\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-GB,en;q=0.5\nAccept-Encoding: gzip, deflate\nConnection: keep-alive\nUpgrade-Insecure-Requests: 1")
data = c.recv(6064)
print (repr(data))
c.close()
