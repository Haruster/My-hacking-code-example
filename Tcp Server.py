#Tcp Server
import socket
host = "127.0.0.1"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
(data, addr) = s.recvfrom(1024)
print "Received from", addr
print "Obtained", data
s.close()
